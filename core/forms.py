from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto:{assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='emaisl venvl',
            body=conteudo,
            from_email='contato@seudomino.com',
            to=['contato@seudominio.com'],
            headers={'Reply-To':email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome' ,'preco' ,'estoque' ,'imagem' ]
