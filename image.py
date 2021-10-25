class image:
  file_name=["F8-107-1.jpg","F8-107-1 (2).jpg","F8-107-1 (3).jpg","F10-136-1.jpg","F10-136-2.jpg"]

  def load(img_name):
    img_path=path_prefix + img_name
    img=image.load_img(img_path,target_size=(300,300))
    img=image.img_to_array(img)
    images.append(imread(img_path))
    inputs.append(img.copy())
    inputs=images_loading(image_path)
    return inputs

  for file in file_name:
    load(file)
