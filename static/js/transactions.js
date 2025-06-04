// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#transaction_form');

    // Basic form validation before submission
    form.addEventListener('submit', function (event) {
        const amount = parseFloat(form.amount.value);
        if (isNaN(amount) || amount <= 0) {
            alert("Please enter a valid amount greater than 0.");
            event.preventDefault(); // Stop form from submitting
        }

        const currency = form.currency.value.trim();
        if (!currency || currency.length !== 3) {
            alert("Please enter a valid 3-letter currency code (e.g., USD).");
            event.preventDefault();
        }
    });

    // // Optional: Live update for transaction type styling
    // const typeSelect = form.querySelector('select[name="transaction_type"]');
    // typeSelect.addEventListener('change', function () {
    //     form.style.borderColor = typeSelect.value === "income" ? "green" : "red";
    // });


    const categoryFilter = document.getElementById("categoryFilter");
    const rows = document.querySelectorAll("tbody tr");
    categoryFilter.addEventListener('change',() => {
        const selectedVAlue = categoryFilter.value.toLowerCase();
        rows.forEach(row =>{
            const rowCat = row.getAttribute('data-category')?.toLowerCase();
            if (!selectedVAlue||rowCat === selectedVAlue){
                row.style.display = '';}
            else{
                row.style.display = 'none';
            }
        })
    })
    
    
    
    // Example: Add animation to table rows on load
    rows.forEach((row, index) => {
        row.style.opacity = 0;
        setTimeout(() => {
            row.style.transition = "opacity 0.5s ease";
            row.style.opacity = 1;
        }, index * 100);
    });
});
