from django.db import models
from account.models import User

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    mobile = models.IntegerField()
    textarea = models.CharField(max_length=400)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    author = models.CharField(max_length=100, default='')
    bookformat = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=1000, default='')
    genre = models.CharField(max_length=200, default='')
    img = models.ImageField(upload_to='product/')
    isbn = models.CharField(max_length=50, default='')
    link= models.CharField(max_length=200, default='')
    pages= models.IntegerField(default=0)
    rating= models.IntegerField(default=0)
    title = models.CharField(max_length=100,default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return (str(self.id) + " "+self.title)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_detail(id=0):
        return Product.objects.get(id=id)

    @staticmethod
    def get_detail_isbn(isbn):
        return Product.objects.get(isbn=isbn)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} in Order {self.order.id}"
  

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)