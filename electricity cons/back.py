from flask import Flask, request, jsonify, send_from_directory
import math
import statistics
import os

app = Flask(__name__)


# ==========================================
# SERVE HTML
# ==========================================

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# ==========================================
# SERVE CSS
# ==========================================

@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")


# ==========================================
# ANALYZE ELECTRICITY DATA
# ==========================================

@app.route("/api/analyze", methods=["POST"])
def analyze():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No data received."
            }), 400


        records = data.get("records", [])


        if not records:

            return jsonify({
                "success": False,
                "error": "No electricity records available."
            }), 400


        # --------------------------------------
        # Clean and calculate records
        # --------------------------------------

        processed = []


        for item in records:

            month = str(
                item.get("month", "")
            ).strip()


            units = float(
                item.get("units", 0)
            )


            rate = float(
                item.get("rate", 0)
            )


            if units < 0 or rate < 0:

                return jsonify({
                    "success": False,
                    "error": "Units and rate cannot be negative."
                }), 400


            bill = units * rate


            processed.append({

                "month": month,
                "units": units,
                "rate": rate,
                "bill": bill

            })


        # --------------------------------------
        # Values
        # --------------------------------------

        units = [
            item["units"]
            for item in processed
        ]


        bills = [
            item["bill"]
            for item in processed
        ]


        # --------------------------------------
        # Basic calculations
        # --------------------------------------

        total_units = sum(units)

        average_units = (
            total_units / len(units)
        )


        total_bill = sum(bills)

        average_bill = (
            total_bill / len(bills)
        )


        # --------------------------------------
        # Highest / lowest consumption
        # --------------------------------------

        max_units = max(units)

        min_units = min(units)


        max_consumption_item = max(
            processed,
            key=lambda x: x["units"]
        )


        min_consumption_item = min(
            processed,
            key=lambda x: x["units"]
        )


        # --------------------------------------
        # Highest / lowest bill
        # --------------------------------------

        max_bill_item = max(
            processed,
            key=lambda x: x["bill"]
        )


        min_bill_item = min(
            processed,
            key=lambda x: x["bill"]
        )


        # --------------------------------------
        # Statistics
        # --------------------------------------

        mean = statistics.mean(units)

        median = statistics.median(units)


        if len(units) > 1:

            standard_deviation = statistics.pstdev(
                units
            )

        else:

            standard_deviation = 0


        # --------------------------------------
        # Return everything
        # --------------------------------------

        return jsonify({

            "success": True,

            "records": processed,

            "dashboard": {

                "totalConsumption": total_units,

                "averageConsumption": average_units,

                "totalBill": total_bill,

                "monthsRecorded": len(processed)

            },

            "analysis": {

                "maxConsumption": max_units,

                "maxMonth":
                    max_consumption_item["month"],

                "minConsumption": min_units,

                "minMonth":
                    min_consumption_item["month"],

                "maxBill":
                    max_bill_item["bill"],

                "maxBillMonth":
                    max_bill_item["month"],

                "minBill":
                    min_bill_item["bill"],

                "minBillMonth":
                    min_bill_item["month"]

            },

            "statistics": {

                "total": total_units,

                "mean": mean,

                "median": median,

                "maximum": max(units),

                "minimum": min(units),

                "standardDeviation":
                    standard_deviation

            },

            "charts": {

                "months": [
                    item["month"]
                    for item in processed
                ],

                "consumption": units,

                "bills": bills

            }

        })


    except Exception as error:

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500


# ==========================================
# APPLIANCE CALCULATION
# ==========================================

@app.route("/api/appliances", methods=["POST"])
def appliances():

    try:

        data = request.get_json()

        appliances_data = data.get(
            "appliances",
            []
        )


        total = 0

        highest = None

        lowest = None


        for appliance in appliances_data:

            name = appliance.get(
                "name",
                "Unknown"
            )


            power = float(
                appliance.get(
                    "power",
                    0
                )
            )


            hours = float(
                appliance.get(
                    "hours",
                    0
                )
            )


            days = float(
                appliance.get(
                    "days",
                    0
                )
            )


            if (
                power <= 0
                or hours <= 0
                or days <= 0
            ):

                continue


            # Units =
            # Power × Hours × Days / 1000

            units = (
                power *
                hours *
                days
            ) / 1000


            total += units


            current = {

                "name": name,

                "units": units

            }


            if (
                highest is None
                or units > highest["units"]
            ):

                highest = current


            if (
                lowest is None
                or units < lowest["units"]
            ):

                lowest = current


        if highest is None:

            return jsonify({

                "success": False,

                "error":
                    "Please enter appliance details."

            })


        return jsonify({

            "success": True,

            "total": total,

            "highest": highest,

            "lowest": lowest

        })


    except Exception as error:

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":

    app.run(

        host="127.0.0.1",

        port=5000,

        debug=True

    )