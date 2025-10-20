document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById("chartInmuebles")?.getContext("2d");
    if (!ctx) return;

    const disponibles = parseInt(document.getElementById("disponibles")?.textContent || 0);
    const rentados = parseInt(document.getElementById("rentados")?.textContent || 0);

    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["Disponibles", "Rentados"],
            datasets: [{
                data: [disponibles, rentados],
                backgroundColor: ["#16a34a", "#ca8a04"],
            }],
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "bottom",
                },
            },
        },
    });
});