from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort

mod = Blueprint('general', __name__)


@mod.route("/admin/admin-edit-product/<int:product_id>", methods=['GET', 'POST'])
def admin_edit_product(product_id):
    form, path = FormProduct(), get_path()
    product = get_product(product_id)
    message, result, filenames = None, False, []
    if "message" not in product:
        if request.method == 'POST':
            filenames = save_images(request.files, path, current_user.email, max_image=15)
            chimg = list(map(lambda x: x.split("/")[-1], filenames)) != list(map(lambda x: x.split("/")[-1], product["images"].split("//")))
            message = put_product(current_user.email, product_id, {"status": form.status.data, "price": form.price.data,
                                                                   "description": form.description.data, "chimg": chimg,
                                                                   "upholstery": form.upholstery.data, "lining": form.lining.data,
                                                                   "mechanism": form.mechanism.data, "roller": form.roller.data,
                                                                   "name": form.name.data})
            if "success" in message:
                filenames = copy_files(path, f"product/product_{product_id}", filenames)
                m = put_product(current_user.email, product_id, {"images": "//".join(filenames)})
                result = True
                set_special_params()
            message = list(message.values())[-1]
        else:
            form.name.data = product["name"]
            form.description.data = product["description"]
            form.status.data = product["status"]
            form.price.data = product["price"]
            form.upholstery.data = product["upholstery"]
            form.lining.data = product["lining"]
            form.mechanism.data = product["mechanism"]
            form.roller.data = product["roller"]
            filenames = copy_files(f"product/product_{product_id}", path, product["images"].split("//"))
            admin_images[current_user.email] = [_.split("/")[-1] for _ in filenames]
    else:
        message = list(product.values())[-1]
    return get_render_template('form/form-product.html', title='Редактирование товара', message=message, form=form,
                               result=result, filenames=filenames, image_len=len(filenames) + 1)
