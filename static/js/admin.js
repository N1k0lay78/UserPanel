let max_count = 0;
let image_id = 0;

function on_start() {
    if (document.getElementsByClassName("form__images").length !== 0) {
        max_count = parseInt(document.getElementsByClassName("form__images")[0].getAttribute("data-count"));
        image_id = document.getElementsByClassName("form__images")[0].childElementCount + 1;
        check_images_empty();
    }
}

on_start();

function on_change_image_input() {
    if (this.files && this.files[0]) {
        let parent = this.parentElement;
        let fr = new FileReader();
        fr.onload = function () {
            parent.getElementsByClassName("form__icon-preview")[0].setAttribute("src", fr.result);
            check_images_empty();
            parent.getElementsByClassName("form__icon-delete")[0].classList.remove("hidden");
        }
        fr.readAsDataURL(this.files[0]);
    }
}

function delete_image() {
    let parent = this.parentElement.parentElement;
    parent.remove();
    check_images_empty()
}

let all_input_images = document.getElementsByClassName("form__icon");
for (let i=0; i < all_input_images.length; i++) {
    all_input_images[i].addEventListener("change", on_change_image_input);
}

let buttons_delete = document.getElementsByClassName("form__icon-delete");
for (let i=0; i < buttons_delete.length; i++) {
    buttons_delete[i].addEventListener("click", delete_image);
}

function add_image(form_images) {
    element = document.createElement("div");
    element.classList.add("form__icon-wrapper");
    element.innerHTML = "<div class=\"form__icon-container\"><img src=\"/static/img/plus.svg\" alt=\"\" class=\"form__icon-preview\"><input type=\"file\" name=\"image_" + image_id + "\" class=\"form__icon\"><div class=\"form__icon-delete hidden\"></div></div>";
    element.getElementsByClassName("form__icon")[0].addEventListener("change", on_change_image_input);
    element.getElementsByClassName("form__icon-delete")[0].addEventListener("click", delete_image);
    image_id += 1;
    form_images.appendChild(element);
}

function check_images_empty() {
    let images_container = document.getElementsByClassName("form__images")[0];
    if (images_container.children[images_container.children.length - 1].getElementsByClassName("form__icon-preview")[0].getAttribute("src") !== "/static/img/plus.svg"
        && images_container.childElementCount < max_count) {
        add_image(images_container);
    }
}

function view_password() {
    this.classList.toggle("hide");
    let password = this.parentElement.getElementsByClassName("form__input")[0];
    if (password.getAttribute("type") === "password") {
        password.setAttribute("type", "text");
    } else {
        password.setAttribute("type", "password");
    }
}

let view_buttons = document.getElementsByClassName("eye-button");
for (let i = 0; i < view_buttons.length; i++) {
    view_buttons[i].addEventListener("click", view_password);
}