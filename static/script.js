document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('churnForm');
    
    form.addEventListener('submit', (event) => {
        // Add any custom validation logic here
        // Example: ensure that all inputs are either 0 or 1
        const inputs = form.querySelectorAll('input[type="number"]');
        let valid = true;
        
        inputs.forEach(input => {
            if (input.name !== 'tenure' && input.name !== 'MonthlyCharges' && (input.value < 0 || input.value > 1)) {
                valid = false;
            }
        });
        
        if (!valid) {
            event.preventDefault();
            alert('Please enter valid inputs (0 or 1 for categorical fields, valid numbers for tenure and charges).');
        }
    });
});
