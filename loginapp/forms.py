from django import forms
class RegistrationForm(forms.Form):
    firstname=forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your First Name',
                'class':'form-control'
            }
        )
    )
    lastname=forms.CharField(
        label="Enter Your Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Last Name',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'User Name',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Your Password',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Your Mobile Number',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Your Email ID',
                'class':'form-control'
            }
        )
    )
    GENDER_CHOICES=(
        ('MALE','male'),
        ('FEMALE','female')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),
            choices=GENDER_CHOICES,
            label="Select Your Gender"
    )
    y=range(1960,2020)
    date_of_birth=forms.DateField(
        widget=forms.SelectDateWidget(years=y),
        label="Enter Your Date Of Birth"
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Enter Your User Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Your Password',
                'class': 'form-control'
            }
        )
    )

class InsertingData(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Product TD",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product ID',
                'class': 'form-control'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter Product Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product Name',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter Product Class",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product Class',
                'class': 'form-control'
            }
        )
    )
    no_of_products=forms.IntegerField(
        label="Enter Number Of Products",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Number Of Products',
                'class': 'form-control'
            }
        )
    )

    customer_name=forms.CharField(
        label="Enter Customer Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Customer Name',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile Number',
                'class':'form-control'

            }
        )
    )
    email=forms.EmailField(
        label="Enter Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email ID',
                'class':'form-control'
            }
        )
    )
    y = range(2000, 2020)
    manufacture_date = forms.DateField(
        label="Manufacture Date",
        widget=forms.SelectDateWidget(years=y)
    )
    expiry_date = forms.DateField(
        label="Select Expiry Date",
        widget=forms.SelectDateWidget()
    )

class UpdateData(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product TD",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product ID',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )

class DeletingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product TD",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product ID',
                'class': 'form-control'
            }
        )
    )


from django import forms

class InsertingData(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Product TD",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product ID',
                'class': 'form-control'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter Product Name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product Name',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter Product Class",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Product Class',
                'class': 'form-control'
            }
        )
    )
    no_of_products=forms.IntegerField(
        label="Enter Number Of Products",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Number Of Products',
                'class': 'form-control'
            }
        )
    )

    customer_name=forms.CharField(
        label="Enter Customer Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Customer Name',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile Number',
                'class':'form-control'

            }
        )
    )
    email=forms.EmailField(
        label="Enter Email ID",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email ID',
                'class':'form-control'
            }
        )
    )
    y = range(2000, 2020)
    manufacture_date = forms.DateField(
        label="Manufacture Date",
        widget=forms.SelectDateWidget(years=y)
    )
    expiry_date = forms.DateField(
        label="Select Expiry Date",
        widget=forms.SelectDateWidget()
    )

class UpdateData(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product TD",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product ID',
                'class': 'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product Cost',
                'class': 'form-control'
            }
        )
    )

class DeletingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product TD",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product ID',
                'class': 'form-control'
            }
        )
    )