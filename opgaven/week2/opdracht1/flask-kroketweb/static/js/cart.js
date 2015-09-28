var cart = {};

function inputAddEventListeners(inputs){
inputs.forEach(function (input) {
    input.addEventListener("focusout", function (e) {
        totalsum = 0;

        if (!this.value.match(/^[0-9]+$/)) {
            this.value = "";
        }

        var amount = this.value;
        var product = this.parentNode.parentNode.querySelector("td:first-of-type").textContent;
        var price = this.parentNode.parentNode.querySelector("td:nth-of-type(2)").textContent;

        var total = parseInt(amount) * parseFloat(price.replace(",", "."));
        total = total.toFixed(2);

        if (amount.length > 0) {
            cart[product] = {
                product: product,
                amount: amount,
                price: price,
                total: total
            }
            sessionStorage.setItem(product, JSON.stringify(cart[product]));
        }
        else {
            delete cart[product];
            sessionStorage.removeItem(product);
             }

        renderCart();
    });
});
};

function renderCart() {
    var tbody = document.querySelector("table.cart tbody");

    while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
    }

    if(sessionStorage.length > 0 )
    {
        for (var key in sessionStorage) {
            var product = JSON.parse(sessionStorage[key]);
            console.log(product)
            tbody.appendChild(renderCartEntry(product));
        }
        tbody.appendChild(renderCartTotalPrice());
    }else{
         tbody.appendChild(document.createElement("td"));
    }
}

function renderCartEntry(cartItem) {
    var row = document.createElement("tr");
    var columns = [
        cartItem.product,
        cartItem.amount,
        cartItem.price,
        cartItem.total
    ];

    totalsum += parseFloat(cartItem.total);
    totalsum = parseFloat(totalsum.toFixed(3));

    columns.forEach(function (column) {
        var col = document.createElement("td");
        col.innerHTML = column;
        row.appendChild(col);
    });

    return row;
}

function renderCartTotalPrice() {
    var row = document.createElement("tr");

    var col = document.createElement("td");
    col.innerHTML = "Prijs totale bestelling";
    row.appendChild(col);

    var col = document.createElement("td");
    col.innerHTML = totalsum;
    row.appendChild(col);

    return row;

}

$(function() {
    $('#btnAfrekenen').click(function() {
        
        $.ajax({
            url: '/sendOrder',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

       CREATE TABLE `kroketweb`.`customer` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(45) NULL,
  `user_address` VARCHAR(45) NULL,
  `user_city` VARCHAR(45) NULL,
  `user_phonenumber` VARCHAR(45) NULL,
  PRIMARY KEY (`user_id`));


  DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createCustomer`(
    IN p_name VARCHAR(20),
    IN p_address VARCHAR(20),
    IN p_city VARCHAR(20),
    IN p_phonenumber VARCHAR(20)
)
BEGIN
    if ( select exists (select 1 from customer where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into customer
        (
            user_name,
            user_address,
            user_city,
            user_phonenumber
        )
        values
        (
            p_name,
            p_address,
            p_city,
            p_phonenumber
        );
     
    END IF;
END$$
DELIMITER ;