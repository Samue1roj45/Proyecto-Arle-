document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById("chartInmuebles").getContext("2d");

    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["Disponibles", "Vendidos", "Rentados"],
            datasets: [{
                data: [parseInt(document.getElementById("disponibles")?.textContent || 0),
                       parseInt(document.getElementById("vendidos")?.textContent || 0),
                       parseInt(document.getElementById("rentados")?.textContent || 0)],
                backgroundColor: ["#16a34a", "#dc2626", "#ca8a04"]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
});