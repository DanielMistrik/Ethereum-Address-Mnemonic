$('#EthOut').on('submit', function(e){
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: post_link_2,
            data: {
                mnem: $('#mnemonic').val(),
                csrfmiddlewaretoken: csrf_token_2,
                dataType: "json",
            },
            success: function (data) {
                if (document.getElementById("validicon2").style.display == 'block'){
                    document.getElementById("AddressOutput").textContent = data.msg;
                    document.getElementById("copyMnemButton").style.visibility = 'visible';
                }
                else{
                    document.getElementById("AddressOutput").textContent = 'Invalid Mnemonic';
                }
                document.getElementById("AddressOutput").style = "font-size: 20px;";
            },
            failure: function () {
            }
        });
});