

function renderProducts(products) {
    var tbody = document.querySelector("table.producten tbody");
    while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
    }
    console.log(JSON.parse(products)[0].Prijs)
    for (var item in products) {
        var product = JSON.parse(products[item]);
        tbody.appendChild(renderProductEntry(product));
    }
}

function renderProductEntry(product) {
    var row = document.createElement("tr");
    var columns = [
        cartItem.product,
        cartItem.amount,
        cartItem.price,
        cartItem.total
    ];

    console.log("nummer");
    totalsum += parseFloat(cartItem.total.replace(",", "."));


    columns.forEach(function (column) {
        var col = document.createElement("td");
        col.innerHTML = column;
        row.appendChild(col);
    });

    return row;
}
