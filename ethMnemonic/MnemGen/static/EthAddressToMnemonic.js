$('#EthIn').on('submit', function(e){
e.preventDefault();
    $.ajax({
        type: "POST",
        url: post_link_1,
        data: {
            addrss: $('#ethAddress').val(),
            csrfmiddlewaretoken: csrf_token_1,
            dataType: "json",
        },
        success: function (data) {
            if (document.getElementById("validicon").style.display == 'block'){
                    document.getElementById("MnemonicOutput").textContent = data.msg;
                    document.getElementById("copyAddressButton").style.visibility = 'visible';
                }
                else{
                    document.getElementById("MnemonicOutput").textContent = 'Invalid Address';
                }
            document.getElementById("MnemonicOutput").style = "font-size: 20px;";
        },
        failure: function () {
        }
    });
});
