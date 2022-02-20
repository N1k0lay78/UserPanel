function on_change_image_input() {
    if (this.files && this.files[0]) {
        let parent = this.parentElement;
        let fr = new FileReader();
        fr.onload = function () {
            // console.log(parent)
            parent.getElementsByClassName("form__icon-preview")[0].setAttribute("src", fr.result);
            check_images_empty();
        }
        fr.readAsDataURL(this.files[0]);
    }
}

function delete_image() {
    let parent = this.parentElement;
    parent.getElementsByClassName("form__icon-preview")[0].removeAttribute('src');
    parent.getElementsByClassName("form__icon")[0].type = "text";
    parent.getElementsByClassName("form__icon")[0].type = "file";
    let image_inputs = parent.parentElement.parentElement.getElementsByClassName("form__icon-container");
    let start_swap = false;
    for (let i = 0; i < image_inputs.length - 1; i++) {
        if (image_inputs[i] === parent) {
            start_swap = true;
        }
        if (start_swap) {
            image_inputs[i].getElementsByClassName("form__icon-preview")[0].setAttribute("src", image_inputs[i+1].getElementsByClassName("form__icon-preview")[0].getAttribute("src"));
            image_inputs[i].getElementsByClassName("form__icon")[0].files = image_inputs[i+1].getElementsByClassName("form__icon")[0].files;
            image_inputs[i+1].getElementsByClassName("form__icon-preview")[0].removeAttribute('src');
            image_inputs[i+1].getElementsByClassName("form__icon")[0].type = "text";
            image_inputs[i+1].getElementsByClassName("form__icon")[0].type = "file";
        }
    }
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

function check_images_empty() {
    let images_input = document.getElementsByClassName("form__images");
    for (let i=0; i < images_input.length; i++) {
        let children = images_input[0].children;
        let is_first = true;
        for (let j=0; j < children.length; j++) {
            console.log(children[j].getElementsByClassName("form__icon")[0].files)
            if (!children[j].getElementsByClassName("form__icon")[0].files[0]) {
                children[j].getElementsByClassName("form__icon-delete")[0].classList.add("hidden");
                if (is_first) {
                    children[j].classList.remove("hidden");
                    children[j].getElementsByClassName("form__icon-preview")[0].setAttribute("src", "/static/img/plus.svg");
                    is_first = false;
                } else {
                    children[j].classList.add("hidden");
                }
            } else {
                children[j].classList.remove("hidden");
                children[j].getElementsByClassName("form__icon-delete")[0].classList.remove("hidden");
            }
        }
    }
    let icon_input = document.getElementsByClassName("form__icons");
    for (let i = 0; i < icon_input.length; i++) {
        let icon = icon_input[i].children[0];
        if (icon.getElementsByClassName("form__icon-preview")[0].getAttribute("src") === "") {
            icon.getElementsByClassName("form__icon-preview")[0].setAttribute("src", "/static/img/plus.svg");
        }
    }
}

check_images_empty();

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