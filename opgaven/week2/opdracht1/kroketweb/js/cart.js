var cart = {};

var inputs = document.querySelectorAll(".producten input");

inputs = Array.prototype.slice.call(inputs);

inputs.forEach(function(input) {
	input.addEventListener("focusout", function(e){
		var amount = this.value;
		var product = this.parentNode.parentNode.querySelector("td:first-of-type").textContent;
		var price = this.parentNode.parentNode.querySelector("td:nth-of-type(2)").textContent;
		
		var total = parseInt(amount) * parseFloat(price.replace(",", "."));
		total = total.toFixed(2);

		if(amount.length > 0)
		{
			cart[product] = {
				product:product, 
				amount: amount, 
				price: price,
				total: total
			}
		}
		else{
			delete cart[product];
		}

		renderCart(cart);
	});
});

function renderCart(cart) {
	var tbody = document.querySelector("table.cart tbody");

	while(tbody.hasChildNodes()) {
		tbody.removeChild(tbody.lastChild);
	}

	for(var key in cart) {
		var product = cart[key];
		tbody.appendChild(renderCartEntry(product));
	}
}

function renderCartEntry(cartItem){
	var row = document.createElement("tr");
	var columns = [
		cartItem.product,
		cartItem.amount,
		cartItem.price,
		cartItem.total
	];

	columns.forEach(function(column) {
		var col = document.createElement("td");
		col.innerHTML = column;
		row.appendChild(col);
	});

	return row;
}