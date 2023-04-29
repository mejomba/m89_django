import re
from django.shortcuts import render
from .models import Product


def images_address(data):
    url_pattern = r'^(.*[\\\/])[^\\\/]*$'
    image_pattern = r'([^\/]+$)'
    print(str(data.url))
    # image = re.split(image_pattern, str(data.url), maxsplit=5)
    url = re.findall(url_pattern, data.url)[0]
    images = [list(map(lambda img: url + img, str(item.group()).split('%2C'))) for item in re.finditer(image_pattern, data.url)][0]
    print(url)
    return images


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        count = request.POST.get('count')
        name = request.POST.get('name')
        price = request.POST.get('price')

        out = ','.join(str(img) for img in images)
        Product.objects.create(image=out, count=count, name=name, price=price)

        for image in images:
            file = open('/media/image', 'wb')
            # file.write(image.file)
            print(image.__dict__)
            print(image.file)
            print('#' * 29)
            # Product.objects.create(image=image, count=count, name=name, price=price)

    images = Product.objects.all()
    # for img in images:
    #     img.image = images_address(img.image)
    #     print('#' * 29)
    #     print(img.image)
    #     print('#' * 29)

    return render(request, 'shop/upload_test.html', {'images': images})
