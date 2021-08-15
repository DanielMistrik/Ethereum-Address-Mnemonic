$('#EthOut').on('submit', function(e){
e.preventDefault();
$.ajax({
    type : "POST",
    url: post_link_2,
    data: {
        mnem : $('#mnemonic').val(),
        csrfmiddlewaretoken: csrf_token_2,
        dataType: "json",
    },
    success: function(data){
        document.getElementById("copyMnemButton").style.visibility = 'visible';
        document.getElementById("AddressOutput").textContent = data.msg;
        document.getElementById("AddressOutput").style = "font-size: 20px;";
    },
    failure: function() {
    }
        });
});