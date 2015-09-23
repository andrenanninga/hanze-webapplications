var totalsum = 0;

 $(function() {
        $.ajax({
            url: '/getProducts',
            type: 'GET',
            success: function(res) {
              renderProducts(JSON.parse(res));
            },
            error: function(error) {
                console.log(error);
            }
        });
    });


function renderProducts(products) {
    var tbody = document.querySelector("table.producten tbody");
    while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
    }
    for (var item in products) {
        var product = products[item];
        tbody.appendChild(renderProductEntry(product));
    }

    var inputs = document.querySelectorAll(".producten input");
    inputs = Array.prototype.slice.call(inputs);
    inputAddEventListeners(inputs);

}

function renderProductEntry(product) {
    var row = document.createElement("tr");
    var columns = [
        product.Omschrijving,
        product.Prijs,
        product.Voorraad,
    ];


    columns.forEach(function (column) {
        var col = document.createElement("td");
        col.type="column"
        col.innerHTML = column;
        row.appendChild(col);
    });

    var col = document.createElement("td");
    var inputBox = document.createElement("input");
    inputBox.type = "input";
    inputBox.size = "3";
    col.appendChild(inputBox)
    row.appendChild(col)
    return row;
}