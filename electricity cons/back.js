// ============================================
// ELECTRICITY CONSUMPTION ANALYZER
// script.js
// ============================================


// ============================================
// DATA STORAGE
// ============================================

let electricityData =
    JSON.parse(localStorage.getItem("electricityData")) || [];

let consumptionChart = null;
let billChart = null;


// ============================================
// INITIALIZE WEBSITE
// ============================================

document.addEventListener("DOMContentLoaded", function () {

    updateDashboard();
    updateTable();
    updateGraphs();

});


// ============================================
// ADD MONTHLY DATA
// ============================================

document
    .getElementById("electricityForm")
    .addEventListener("submit", function (event) {

        event.preventDefault();

        const month =
            document.getElementById("month").value.trim();

        const units =
            Number(document.getElementById("units").value);

        const rate =
            Number(document.getElementById("rate").value);


        if (!month) {

            alert("Please enter a month.");
            return;

        }


        if (units < 0 || rate < 0) {

            alert("Values cannot be negative.");
            return;

        }


        if (units === 0 || rate === 0) {

            alert("Units and rate must be greater than 0.");
            return;

        }


        const bill = units * rate;


        electricityData.push({

            month: month,
            units: units,
            rate: rate,
            bill: bill

        });


        saveData();


        this.reset();


        updateDashboard();

        updateTable();

        updateGraphs();

    });


// ============================================
// SAVE DATA
// ============================================

function saveData() {

    localStorage.setItem(
        "electricityData",
        JSON.stringify(electricityData)
    );

}


// ============================================
// UPDATE DASHBOARD
// ============================================

function updateDashboard() {

    if (electricityData.length === 0) {

        document.getElementById(
            "totalConsumption"
        ).textContent = "0 Units";


        document.getElementById(
            "averageConsumption"
        ).textContent = "0 Units";


        document.getElementById(
            "totalBill"
        ).textContent = "₹0";


        document.getElementById(
            "monthsRecorded"
        ).textContent = "0";


        document.getElementById(
            "maxConsumption"
        ).textContent = "0 Units";


        document.getElementById(
            "minConsumption"
        ).textContent = "0 Units";


        document.getElementById(
            "maxBill"
        ).textContent = "₹0";


        document.getElementById(
            "minBill"
        ).textContent = "₹0";


        updateStatistics([]);

        return;

    }


    const units =
        electricityData.map(item => item.units);


    const bills =
        electricityData.map(item => item.bill);


    const total =
        units.reduce(
            (sum, value) => sum + value,
            0
        );


    const average =
        total / units.length;


    const totalBill =
        bills.reduce(
            (sum, value) => sum + value,
            0
        );


    const max =
        Math.max(...units);


    const min =
        Math.min(...units);


    const maxIndex =
        units.indexOf(max);


    const minIndex =
        units.indexOf(min);


    const maxBill =
        Math.max(...bills);


    const minBill =
        Math.min(...bills);


    const maxBillIndex =
        bills.indexOf(maxBill);


    const minBillIndex =
        bills.indexOf(minBill);


    document.getElementById(
        "totalConsumption"
    ).textContent =
        total.toFixed(2) + " Units";


    document.getElementById(
        "averageConsumption"
    ).textContent =
        average.toFixed(2) + " Units";


    document.getElementById(
        "totalBill"
    ).textContent =
        "₹" + totalBill.toFixed(2);


    document.getElementById(
        "monthsRecorded"
    ).textContent =
        electricityData.length;


    document.getElementById(
        "maxConsumption"
    ).textContent =
        max.toFixed(2) + " Units";


    document.getElementById(
        "maxMonth"
    ).textContent =
        electricityData[maxIndex].month;


    document.getElementById(
        "minConsumption"
    ).textContent =
        min.toFixed(2) + " Units";


    document.getElementById(
        "minMonth"
    ).textContent =
        electricityData[minIndex].month;


    document.getElementById(
        "maxBill"
    ).textContent =
        "₹" + maxBill.toFixed(2);


    document.getElementById(
        "maxBillMonth"
    ).textContent =
        electricityData[maxBillIndex].month;


    document.getElementById(
        "minBill"
    ).textContent =
        "₹" + minBill.toFixed(2);


    document.getElementById(
        "minBillMonth"
    ).textContent =
        electricityData[minBillIndex].month;


    updateStatistics(units);

}


// ============================================
// UPDATE TABLE
// ============================================

function updateTable() {

    const table =
        document.getElementById("dataTable");


    table.innerHTML = "";


    if (electricityData.length === 0) {

        table.innerHTML = `

            <tr>

                <td colspan="6" class="empty">

                    No electricity data available.

                </td>

            </tr>

        `;

        return;

    }


    electricityData.forEach(function (item, index) {

        let status = "Normal";


        if (item.units > 300) {

            status = "High";

        }


        const row =
            document.createElement("tr");


        row.innerHTML = `

            <td>${index + 1}</td>

            <td>${item.month}</td>

            <td>${item.units.toFixed(2)} Units</td>

            <td>₹${item.rate.toFixed(2)}</td>

            <td>₹${item.bill.toFixed(2)}</td>

            <td>

                <span class="status">

                    ${status}

                </span>

            </td>

        `;


        table.appendChild(row);

    });

}


// ============================================
// STATISTICAL ANALYSIS
// ============================================

function updateStatistics(values) {

    if (values.length === 0) {

        document.getElementById(
            "statTotal"
        ).textContent = "0";


        document.getElementById(
            "statMean"
        ).textContent = "0";


        document.getElementById(
            "statMedian"
        ).textContent = "0";


        document.getElementById(
            "statMaximum"
        ).textContent = "0";


        document.getElementById(
            "statMinimum"
        ).textContent = "0";


        document.getElementById(
            "statStd"
        ).textContent = "0";


        return;

    }


    const sorted =
        [...values].sort(
            (a, b) => a - b
        );


    const total =
        values.reduce(
            (sum, value) => sum + value,
            0
        );


    const mean =
        total / values.length;


    const middle =
        Math.floor(sorted.length / 2);


    let median;


    if (sorted.length % 2 === 0) {

        median =
            (sorted[middle - 1] +
                sorted[middle]) / 2;

    } else {

        median =
            sorted[middle];

    }


    const variance =
        values.reduce(
            (sum, value) =>
                sum +
                Math.pow(value - mean, 2),
            0
        ) / values.length;


    const standardDeviation =
        Math.sqrt(variance);


    document.getElementById(
        "statTotal"
    ).textContent =
        total.toFixed(2);


    document.getElementById(
        "statMean"
    ).textContent =
        mean.toFixed(2);


    document.getElementById(
        "statMedian"
    ).textContent =
        median.toFixed(2);


    document.getElementById(
        "statMaximum"
    ).textContent =
        Math.max(...values).toFixed(2);


    document.getElementById(
        "statMinimum"
    ).textContent =
        Math.min(...values).toFixed(2);


    document.getElementById(
        "statStd"
    ).textContent =
        standardDeviation.toFixed(2);

}


// ============================================
// HIGH CONSUMPTION DETECTION
// ============================================

function checkHighConsumption() {

    const limit =
        Number(
            document.getElementById(
                "consumptionLimit"
            ).value
        );


    const output =
        document.getElementById(
            "highConsumptionResult"
        );


    if (electricityData.length === 0) {

        output.innerHTML =
            "Please add electricity data first.";

        return;

    }


    if (
        document.getElementById(
            "consumptionLimit"
        ).value === ""
    ) {

        output.innerHTML =
            "Please enter a consumption limit.";

        return;

    }


    const result =
        electricityData.filter(
            item => item.units > limit
        );


    if (result.length === 0) {

        output.innerHTML =
            "No month has consumption above this limit.";

        return;

    }


    output.innerHTML = `

        <strong>

            ⚠️ High Consumption Months:

        </strong>

        ${result.map(item => `

            <p>

                ${item.month}
                —
                ${item.units.toFixed(2)}
                Units

            </p>

        `).join("")}

    `;

}


// ============================================
// APPLIANCE ANALYSIS
// ============================================

function calculateAppliances() {

    const powerInputs =
        document.querySelectorAll(
            ".appliance-power"
        );


    const hourInputs =
        document.querySelectorAll(
            ".appliance-hours"
        );


    const dayInputs =
        document.querySelectorAll(
            ".appliance-days"
        );


    let total = 0;

    let highest = null;

    let lowest = null;


    powerInputs.forEach(
        function (powerInput, index) {

            const power =
                Number(powerInput.value);


            const hours =
                Number(hourInputs[index].value);


            const days =
                Number(dayInputs[index].value);


            if (
                power <= 0 ||
                hours <= 0 ||
                days <= 0
            ) {

                return;

            }


            const units =
                (power * hours * days) / 1000;


            total += units;


            const appliance =
                powerInput.dataset.appliance;


            if (
                highest === null ||
                units > highest.units
            ) {

                highest = {

                    name: appliance,
                    units: units

                };

            }


            if (
                lowest === null ||
                units < lowest.units
            ) {

                lowest = {

                    name: appliance,
                    units: units

                };

            }

        }
    );


    const output =
        document.getElementById(
            "applianceResult"
        );


    if (highest === null) {

        output.innerHTML = `

            <h3>
                Appliance Analysis Result
            </h3>

            <p>
                Please enter appliance details first.
            </p>

        `;

        return;

    }


    output.innerHTML = `

        <h3>
            Appliance Analysis Result
        </h3>

        <div class="appliance-summary">

            <div>

                <span>
                    Total Consumption
                </span>

                <strong>
                    ${total.toFixed(2)} Units
                </strong>

            </div>


            <div>

                <span>
                    Highest Consuming Appliance
                </span>

                <strong>

                    ${highest.name}

                    (${highest.units.toFixed(2)} Units)

                </strong>

            </div>


            <div>

                <span>
                    Lowest Consuming Appliance
                </span>

                <strong>

                    ${lowest.name}

                    (${lowest.units.toFixed(2)} Units)

                </strong>

            </div>

        </div>

    `;

}


// ============================================
// REAL GRAPHS
// ============================================

function updateGraphs() {

    const consumptionCanvas =
        document.getElementById(
            "consumptionChart"
        );


    const billCanvas =
        document.getElementById(
            "billChart"
        );


    if (!consumptionCanvas || !billCanvas) {

        return;

    }


    if (consumptionChart) {

        consumptionChart.destroy();

    }


    if (billChart) {

        billChart.destroy();

    }


    const labels =
        electricityData.map(
            item => item.month
        );


    const units =
        electricityData.map(
            item => item.units
        );


    const bills =
        electricityData.map(
            item => item.bill
        );


    consumptionChart =
        new Chart(
            consumptionCanvas,
            {

                type: "line",

                data: {

                    labels: labels,

                    datasets: [

                        {

                            label:
                                "Electricity Consumption (Units)",

                            data: units,

                            borderWidth: 3,

                            tension: 0.3,

                            fill: true

                        }

                    ]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    plugins: {

                        legend: {

                            display: true

                        }

                    }

                }

            }
        );


    billChart =
        new Chart(
            billCanvas,
            {

                type: "bar",

                data: {

                    labels: labels,

                    datasets: [

                        {

                            label:
                                "Electricity Bill (₹)",

                            data: bills,

                            borderWidth: 1

                        }

                    ]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    plugins: {

                        legend: {

                            display: true

                        }

                    }

                }

            }
        );

}


// ============================================
// GENERATE REPORT
// ============================================

function generateReport() {

    const output =
        document.getElementById(
            "reportOutput"
        );


    if (electricityData.length === 0) {

        output.innerHTML =
            "<p>Please add electricity data first.</p>";

        return;

    }


    const units =
        electricityData.map(
            item => item.units
        );


    const bills =
        electricityData.map(
            item => item.bill
        );


    const totalUnits =
        units.reduce(
            (sum, value) =>
                sum + value,
            0
        );


    const totalBill =
        bills.reduce(
            (sum, value) =>
                sum + value,
            0
        );


    const averageUnits =
        totalUnits / units.length;


    const averageBill =
        totalBill / bills.length;


    const maxUnits =
        Math.max(...units);


    const minUnits =
        Math.min(...units);


    const maxIndex =
        units.indexOf(maxUnits);


    const minIndex =
        units.indexOf(minUnits);


    output.innerHTML = `

        <h3>
            ⚡ Electricity Consumption Report
        </h3>

        <p>

            <strong>
                Months Recorded:
            </strong>

            ${electricityData.length}

        </p>

        <p>

            <strong>
                Total Consumption:
            </strong>

            ${totalUnits.toFixed(2)}
            Units

        </p>

        <p>

            <strong>
                Average Consumption:
            </strong>

            ${averageUnits.toFixed(2)}
            Units

        </p>

        <p>

            <strong>
                Maximum Consumption:
            </strong>

            ${maxUnits.toFixed(2)}
            Units

            (${electricityData[maxIndex].month})

        </p>

        <p>

            <strong>
                Minimum Consumption:
            </strong>

            ${minUnits.toFixed(2)}
            Units

            (${electricityData[minIndex].month})

        </p>

        <p>

            <strong>
                Total Electricity Bill:
            </strong>

            ₹${totalBill.toFixed(2)}

        </p>

        <p>

            <strong>
                Average Electricity Bill:
            </strong>

            ₹${averageBill.toFixed(2)}

        </p>

    `;

}


// ============================================
// CLEAR DATA
// ============================================

function clearData() {

    if (electricityData.length === 0) {

        alert("No data available to clear.");

        return;

    }


    const confirmClear =
        confirm(
            "Are you sure you want to clear all electricity data?"
        );


    if (!confirmClear) {

        return;

    }


    electricityData = [];


    localStorage.removeItem(
        "electricityData"
    );


    updateDashboard();

    updateTable();

    updateGraphs();


    document.getElementById(
        "reportOutput"
    ).innerHTML = `

        <p>
            Your complete report will appear here.
        </p>

    `;


    document.getElementById(
        "highConsumptionResult"
    ).textContent =
        "Enter a limit to check high consumption.";

}