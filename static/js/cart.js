var updateBtns = document.getElementsByClassName('update-cart')

//Con este script identificamos si el usuario esta registrado o no
//creando dos instancias (usuario registrado / usuario no registraddo)

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)

        console.log('USER: ', user)
        if (user == 'Usuario no identificado'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }

	})
}

function updateUserOrder(productId, action){
    console.log('Usuario identificado, Enviando informacion.....')

        var url = '/update_item/'
        fetch(url, {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken
            },
            body:JSON.stringify({'productId':productId, 'action':action})
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
		   location.reload
		});
}

function addCookieItem (productId, action){
	console.log('Usuario no autentificado')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'qunatity':1}

		}else{
			cart[productId]['qunatity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['qunatity'] -= 1

		if (cart[productId]['qunatity'] <= 0){
			console.log('El elemento a sido eliminado')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}