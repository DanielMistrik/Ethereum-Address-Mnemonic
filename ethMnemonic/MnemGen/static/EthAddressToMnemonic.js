$('#EthIn').on('submit', function(e){
e.preventDefault();
$.ajax({
    type : "POST",
    url: post_link_1,
    data: {
        first_name : $('#ethAddress').val(),
        csrfmiddlewaretoken: csrf_token_1,
        dataType: "json",
    },
    success: function(data){
        $('#MnemonicOutput').value = data.msg;
    },
    failure: function() {
    }
        });

});
