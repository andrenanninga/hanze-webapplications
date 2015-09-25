var totalsum = 0;
var currentPage = 0;

function getProducts(){
 $(function() {
        $.ajax({
            url: '/getProducts',
            type: 'GET',
            success: function(res) {
              localStorage.setItem("products",res);
              renderProducts();
              renderCart();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
}



function renderProducts() {
    var products = JSON.parse(localStorage.getItem("products"));
    var tbody = document.querySelector("table.producten tbody");

    while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
    }

    var productsShowSelect = document.querySelector("select");
    var productsToShow = parseInt(productsShowSelect.value);
    var productPages = products.length / productsToShow;
    var productPageElement = document.querySelector("td.productpagina");

    selectAddEventListeners(productsShowSelect);
    
    while (productPageElement.hasChildNodes()) {
        productPageElement.removeChild(productPageElement.lastChild);
    }
     

    for(var i = 0; i < productPages ;i++){
        var elementTd = document.createElement("td");
        elementTd.value = i;
        elementTd.innerHTML= i + 1;
        productPageElement.appendChild(elementTd);
    }

    var pages = document.querySelectorAll("td.productpagina td");
    pages = Array.prototype.slice.call(pages);
    pagesAddEventListeners(pages);

    console.log(currentPage)

    var currentProductsToIterate = currentPage * productsToShow;

    var i = 0 + currentProductsToIterate;
    if(productsToShow + currentProductsToIterate < products.length){
        var j = productsToShow + currentProductsToIterate;
    }else{
        var j = products.length;
    }


    for(i; i < j ; i++) {
        // for (var item in products) {
            var product = products[i];
            tbody.appendChild(renderProductEntry(product));
        // }
    }

    // Add Input element Listeners
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

function pagesAddEventListeners(pages){
pages.forEach(function (page) {
    page.addEventListener("click", function (e) {
        currentPage = this.value;
        renderProducts();
    });
   });
}

function selectAddEventListeners(selectAmount){
    selectAmount.addEventListener("focusout", function (e) {
        renderProducts();
   });
}