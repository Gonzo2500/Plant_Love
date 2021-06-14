const decreaseBtn = document.querySelectorAll(".decr-btn");
const increaseBtn = document.querySelectorAll(".incr-btn"); 

// Set decrement button style 'inactive' if quantity of an item is 1
decreaseBtn.forEach(btn => {
    if (btn.nextElementSibling.value == 1) {
        btn.style.color = 'gray';
    }
});

// Add increment functionality to '+' button, submit form if quantity is increased
const incrBtn = document.querySelectorAll(".incr-btn");
    // Add click event on all increment buttons
incrBtn.forEach(btn => {
    btn.addEventListener("click", (e) => {
        // Target input element of specific item's form
        let qtySelector = btn.previousElementSibling;
        let qty = parseInt(qtySelector.value);
        // Increase a qty if it's less than 10 and submit a form
        if (qty < 10) {
            // Add active style to decrease button if <10
            decreaseBtn.forEach(btn => {
                btn.style.color = 'black';
            });
            qtySelector.value = qty + 1;
            // submit form
            btn.parentElement.parentElement.submit();
        }
        else {

            btn.style.color = 'gray';
        }
    });
});

// Add decrement functionality to '-' button, submit form if quantity is increased
const decrBtn = document.querySelectorAll(".decr-btn");
decrBtn.forEach(btn => {
    btn.addEventListener("click", (e) => {
        let qtySelector = btn.nextElementSibling;
        let qty = parseInt(qtySelector.value);
        console.log(qty);
        if (qty > 1) {
            increaseBtn.forEach(btn => {
                btn.style.color = 'black';
            });
            qtySelector.value = qty - 1;
            btn.parentElement.parentElement.submit();
        }
        else {
            btn.style.color = 'gray';
        }
    });
}); 