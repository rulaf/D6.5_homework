from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import *


@receiver(m2m_changed, sender=PostCategory)
def post(sender, instance, *args, **kwargs):
    all_sub = Category.objects.all().values_list("subscribers", flat=True)
    categ = Category.objects.all().values_list('name', "subscribers")
    subs = instance.postCategory.values_list("name", flat=True)
    for nc, uid in categ:
        if uid is not None:
            for ct in subs:
                if nc == ct:
                    send_mail(subject=f"{instance.title}",
                              message=f"Здравствуй,{User.objects.get(pk=uid)}."
                                      f" Новая статья в разделе! {ct} \n "
                                      f"Заголовок статьи: {instance.title} \n"
                                      f" Текст статьи: {instance.text[:50]}",
                              from_email='test100skill@gmail.com',
                              recipient_list=[f'{User.objects.get(pk=uid).email}'],
                              )