from django.urls import path
from myapp import views
from myapp.views import views,adminviews
from myapp.views import emailview





urlpatterns = [
    path('checkout',views.checkout,name='checkout.html'),
    path('home',views.home,name='home.html'),
    path('profile',views.profile,name='profile.html'),
    path('login',views.login,name='login.html'),
    path('blog',views.blog,name='blog.html'),
    
    path('insertuser',views.insertuser),
    path('prescription_approval',views.prescription_approval,name='prescription_approval.html'),
    path('register',views.register,name='registration'),
    path('verifying',emailview.verify,name="verify"),
    path('login_user',views.login_user,name='login_user'),
    path('home/<str:login_status>/', views.homes, name='homes'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('logout',adminviews.admin_logout,name='admin_logout'),
    path('logout/',views.logout,name='logout'),
    path('new_password',views.new_password,name='new_password'),
    path('user_image',views.profile_image,name='user_image'),
    
    path('contact_message',views.contact_message,name='contact_message'),
    path('terms',views.terms,name='terms'),
    path('contact',views.contact,name='contact.html'),
    path('forgot',views.forgot,name='forgot.html'),
    path('reset-password',views.reset_password,name='Reset_password'),
    path('changePassword/<token>',emailview.changePassword,name='forgotPassword'),
    path('update_password',views.update_password,name='update_password'),
    path('blog_detail/<int:id>',views.blog_details,name='blog_details'),
    path('blog_comment',views.blog_comment,name='blog_comment'),
    path('delete_comment/<int:comment_id>/<int:blog_id>',views.delete_comment,name='delete_comment'),
    path('blog_edit/<int:id>',adminviews.blog_edit,name='edit_blog'),
    path('update_blog/<int:id>',adminviews.update_blog,name='update_blog'),
    #path('product_page', payment_views.product_page, name='product_page'),
    
     #admin views
    path('dashboard/',adminviews.dashboard,name='dashboard'),
    path('blog_publish',adminviews.blog_publish,name='blog_publish'), # link for publisshing blog
    path('blog_list.html',adminviews.blog_list,name='blog_list'),
    path('blog_post.html',adminviews.blog_post,name='blog_post'),
    path('blog_delete/<int:id>',adminviews.blog_delete,name='blog_delete'),
    path('compose.html',adminviews.compose,name='compose'),
    path('reply.html',adminviews.reply,name='reply'),
    path('chat_drawer.html',adminviews.chat_drawer,name='chat_drawer'),
    path('group_chat.html',adminviews.group_chat,name='group_chat'),
    path('private_chat.html',adminviews.private_chat,name='private_chat'),
    path('invoice2.html',adminviews.invoice2,name='invoice2'),
    path('invoice.html',adminviews.invoice,name='invoice'),
    path('invoice3',adminviews.invoice3,name='invoice3'),
    path('create_invoice.html',adminviews.create_invoice,name='create_invoice'),

    path('customer', adminviews.customer, name = 'customer'),
    path('customer_list.html',adminviews.customer_list,name='customer_list'),
    path('customer_view.html',adminviews.customer_view,name='customer_view'),
    path('customer_message',adminviews.customer_message,name='customer_message'),

    path('contact',adminviews.contact,name='contact'),
    path('add_customer.html',adminviews.add_contact,name='add_contact'),
    path('edit_customer.html',adminviews.edit_contact,name='edit_contact'),
    path('view_customer.html',adminviews.view_contact,name='view_contact'),

    path('files.html',adminviews.files,name='files'),
    path('folder.html',adminviews.folders,name='folders'),
    path('file_manager.html',adminviews.root_directory,name = 'root_directory'),

    path('user_list.html',adminviews.user_list,name='user_list'),
    path('user_view.html',adminviews.user_view,name='user_view'),
    path('permission.html',adminviews.permissions,name='permission'),
    path('role-list.html',adminviews.role_list,name='role_list'),
    path('role-view.html',adminviews.role_view,name='role_view'),

    path('two-factor.html',adminviews.two_factor,name='two_factor'),
    path('signup-html',adminviews.sign_up, name ='sign_up'),
    path('sign-in.html',adminviews.sign_in, name ='sign_in'),
    
    path('reset-password.html',adminviews.reset_password,name='reset_password'),
    path('verify-email.html',adminviews.verify_email,name='verify_email'),
    path('resend_code',views.resend_code,name='resend_code'),
    path('welcome.html',adminviews.welcome_user,name='welcomes'),

    #ecommerce urls
    path('add_category.html',adminviews.add_category, name = 'add_category'),
    path('new_products',adminviews.new_products, name = 'new_product'),

    path('categogries.html',adminviews.categogries, name = 'categogries'),
    path('edit_categories.html',adminviews.edit_categories, name = 'edit_categories'),
    path('edit_products.html',adminviews.product_edit, name = 'edit_products'),
    path('products.html',adminviews.products, name = 'products_list'),
    path('product_edit/<int:id>',adminviews.product_editing,name='product_editing'),
    path('product_update/<int:id>',adminviews.product_update,name='product_update'),
    path('new_products',adminviews.new_products, name = 'new_product'),
    path('uploading',adminviews.upload),
    path('delete_products/<int:id>',adminviews.delete_products,name='delete_products'),
    path('account_deactivate/<int:id>',adminviews.account_deactivate,name='account_deactivate'),
    path('account_activate/<int:id>',adminviews.account_activate,name='account_activate'),

    #frontend cart

    path('products',views.Products, name = 'products'),
    path('order_process',views.order_process,name='order_process'),


    #reports urls
    path('customer_orders.html',adminviews.customer_orders, name = 'customer_orders'),
    #order approval
    path('customer_edit/<int:id>',adminviews.customer_edit,name='customer_edit'),
    path('customer_update/<int:id>',adminviews.customer_update,name='customer_update'),
    path('customer_delete/<int:id>',adminviews.customer_delete,name='customer_delete'),
    path('approval/<int:id>',adminviews.approval,name='approval'),
    #order decline
    path('decline/<int:id>',adminviews.decline,name='decline'),
    path('returns',adminviews.returns, name = 'returns'),
    path('sales',adminviews.sales,name='sales'),
    path('shipping',adminviews.shipping,name='shipping'),
    path('view',adminviews.view,name='view'),
    path('order_items',adminviews.order_items,name='order_items'),
    

    

    path('ecommerce.html', views.ecommerce,name='ecommerce'),
    path('analytics.html', views.analytics_dashboard,name='analytics_dashboard'),
    path('sales.html',adminviews.sales,name='sales.html'),
    
    path('activate/<token>', emailview.activate, name='activate_link'), #link for completing registration
    path('predictions/<int:id>',views.predict_view,name='predictions'),
]
