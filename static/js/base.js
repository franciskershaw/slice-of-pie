// Functions to open and close the wishlist and basket sidebars
$(document).ready( () => {

    // Open wishlist sidebar
    const wishListIcons = document.querySelectorAll('.wishlist-btn');
    const wishListSideBar = document.querySelector('.wishlist-sidebar');
    wishListIcons.forEach((wishListIcon) => {
        wishListIcon.addEventListener('click', () => {
            wishListSideBar.classList.add('sidebar-opened');
        })
    })

    // Open basket
    const basketIcons = document.querySelectorAll('.basket-btn');
    const basketSideBar = document.querySelector('.basket-sidebar');
    basketIcons.forEach((basketIcon) => {
        basketIcon.addEventListener('click', () => {
            basketSideBar.classList.add('sidebar-opened');
        })
    })

    // Close sidebars
    const closeButtons = document.querySelectorAll('.close-sidebar');
    closeButtons.forEach((closeButton) => {
        closeButton.addEventListener('click', () => {
            wishListSideBar.classList.remove('sidebar-opened');
            basketSideBar.classList.remove('sidebar-opened');
        })
    })

})