// Get name of the category from the id and then combine it with MEDIA URL to loop
// through and add background images
const shopButton = document.querySelectorAll('.shop-button');
const mediaUrl = document.querySelector('#id_media_url').innerHTML.slice(1, -1);
shopButton.forEach(btn => {
    const categoryName = btn.innerHTML.toLowerCase();
    btn.style.backgroundImage = `url(${mediaUrl}${categoryName}-btn.png)`;
});


// Sort trigger button
const sort = document.getElementById('sort-trigger');
const container = document.getElementById('sort-container');

sort.addEventListener('click', function () {
    container.classList.toggle('sort-width');
});


const starRating = document.querySelectorAll('.rating-stars');
// Loop through all star rating divs and add star icons depending on the rating
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