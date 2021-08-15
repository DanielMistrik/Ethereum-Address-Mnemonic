$('#EthIn').on('submit', function(e){
    console.log("Here");
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
        $('#MnemonicOutput').html(data.msg) /* response message */
    },
    failure: function() {
    }
        });
});