from django.shortcuts import render, redirect, get_object_or_404
from clinte.models import Cliente
from clinte.forms import ClienteForm
from produto.models import Produto
from produto.forms import ProdutoForm
from vendas.models import Pedido
from vendas.forms import PedidoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	return render(request, 'index.html')

def cliente(request):
	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ClienteForm()
	return render(request, 'core/cliente.html',{'form':form})

def produto(request):
	if request.method == 'POST':
		form = ProdutoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('produto')
	else:
		form = ProdutoForm()
	return render(request, 'core/produtos.html',{'form':form})

def pedido(request):
	if request.method == 'POST':
		form = PedidoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('relatorio')
	else:
		form = PedidoForm()
	return render(request, 'core/pedido.html',{'form':form})

def relatorio(request):
	relatorio = Pedido.objects.all()
	custo = Produto.objects.all()
	paginator = Paginator(relatorio,3)
	page = request.GET.get('page')
	relatorio = paginator.get_page(page)
	return render(request, 'core/relatorio.html',{'relatorio':relatorio,'relatorio':relatorio, 'custo':custo})

def editar(request, id_pedido):
	edite = get_object_or_404(Pedido, id=id_pedido)
	if request.method == 'POST':
		form = PedidoForm(request.POST, instance=edite)
		if form.is_valid():
			form.save()
			return redirect('relatorio')
	else:
		form = PedidoForm(instance=edite)
	return render(request, 'core/pedido.html',{'form':form})

