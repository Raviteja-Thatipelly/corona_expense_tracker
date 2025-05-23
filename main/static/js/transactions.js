document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('transaction_form');
    const categoryFilter = document.getElementById('categoryFilter');
    const rows = document.querySelectorAll('tbody tr');

    // Validate form before submission
    form.addEventListener('submit', function (event) {
        const amount = parseFloat(form.amount.value);
        if (isNaN(amount) || amount <= 0) {
            alert("Please enter a valid amount greater than 0.");
            event.preventDefault();
        }

        const currency = form.currency.value.trim();
        if (!currency || currency.length !== 3) {
            alert("Please enter a valid 3-letter currency code.");
            event.preventDefault();
        }
    });

    // Filter transactions by category
    categoryFilter.addEventListener('change', () => {
        const selectedValue = categoryFilter.value.toLowerCase();
        rows.forEach(row => {
            const rowCat = row.getAttribute('data-category')?.toLowerCase();
            row.style.display = (!selectedValue || rowCat === selectedValue) ? '' : 'none';
        });
    });

    // Animate rows
    rows.forEach((row, index) => {
        row.style.opacity = 0;
        setTimeout(() => {
            row.style.transition = "opacity 0.5s ease";
            row.style.opacity = 1;
        }, index * 100);
    });
});
