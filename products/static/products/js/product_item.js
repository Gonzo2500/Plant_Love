// go back 1 url when back button is clicked, 
const backBtn = document.querySelector('#back-btn');
backBtn.addEventListener('click', (e) => {
    let thisUrl = window.location.href;
    let lastUrl = document.referrer;
    backBtn.setAttribute('onclick', 'history.go(-1)');
    if (thisUrl == lastUrl) {
        history.go(-2);
        console.log(`last url: ${document.referrer}, this url: ${window.location.href}`);
    }
    else {
        history.go(-1);
    }
});

// Set decrement value to 'inactive' by default
document.querySelector(".decr-btn").style.color = 'gray';

// Change price based on quantity argument
let changePrice = qty => {
    const price = document.querySelector("[id^='item-price-'");
    let value = (price.getAttribute("id").split("-"))[2];
    let newValue = value * qty;
    price.innerHTML = `€ ${newValue}.00`;
};


// Display the total price of an item as quantity is changed with arrows 
document.querySelector(".qty-value").addEventListener("change", (event) => {
    let qty = parseInt(event.target.value);
    changePrice(qty);
});

// Add increment functionality to '+' button
let incrBtn = document.querySelector(".incr-btn");
incrBtn.addEventListener("click", (e) => {
    let qtySelector = document.querySelector(".qty-value");
    let qty = parseInt(qtySelector.value);
    if (qty < 10) {
        decrBtn.style.color = 'black';
        qtySelector.value = qty + 1;
        changePrice(qtySelector.value);
    }
    else {
        incrBtn.style.color = 'gray';
    }
});

// Add decrement functionality to '-' button
let decrBtn = document.querySelector(".decr-btn");
decrBtn.addEventListener("click", (e) => {
    let qtySelector = document.querySelector(".qty-value");
    let qty = parseInt(qtySelector.value);
    if (qty > 1) {
        incrBtn.style.color = 'black';
        qtySelector.value = qty -1;
        changePrice(qtySelector.value);
    }
    else {
        decrBtn.style.color = 'gray';
    }
});

const starRating = document.querySelectorAll('.rating-stars');


starRating.forEach(rating => {
    const ratingValue = parseInt(rating.getAttribute('data-value'));
    const fullStar = ratingValue;
    let stars = '';

    for (let i = 1; i < 6; i++) {
        if (i <= fullStar) {
            stars += `<i class="fas fa-star"></i>`;
        }
        else {
            stars += `<i class="far fa-star"></i>`;
        }
    }    
    rating.innerHTML = stars;
});