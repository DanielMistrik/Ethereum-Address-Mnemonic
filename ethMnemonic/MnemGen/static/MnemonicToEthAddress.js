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
        $('#AddressOutput').value =data.msg;/* response message */
    },
    failure: function() {
    }
        });
});