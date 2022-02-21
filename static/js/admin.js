let max_count = 0;
let image_id = 0;

function set_image(url, input){
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        let fileName = 'hasFilename.' + xhr.responseURL.split('.')[xhr.responseURL.split('.').length - 1];
        console.log(fileName);
        let file = new File([xhr.response], fileName,{type:"image/" + xhr.responseURL.split('.')[xhr.responseURL.split('.').length - 1], lastModified:new Date().getTime()}, 'utf-8');
        let container = new DataTransfer();
        container.items.add(file);
        input.files = container.files;
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    xhr.send();
}

function on_start() {
    if (document.getElementsByClassName("form__images").length !== 0) {
        max_count = parseInt(document.getElementsByClassName("form__images")[0].getAttribute("data-count"));
        image_id = document.getElementsByClassName("form__images")[0].childElementCount + 1;
        let inputs = document.getElementsByClassName("form__images")[0].children;
        for (let i = 0; i < inputs.length; i++) {
            set_image(inputs[i].getElementsByClassName("form__icon-preview")[0].getAttribute("src"), inputs[i].getElementsByClassName("form__icon")[0]);
        }
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