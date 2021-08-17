// Function that is called when the mnemonic conversion form is submitted
$('#EthOut').on('submit', function(e){
    e.preventDefault();
    // ajax call that sends the mnemonic and recieves an EIP-55 valid ehtereum address
    $.ajax({
        type: "POST",
        url: post_link_2,
        data: {
            mnem: $('#mnemonic').val(),
            csrfmiddlewaretoken: csrf_token_2,
            dataType: "json",
        },
        // If the ajax function is successful inform the user accordingly
        success: function (data) {
            // If the input mnemonic was valid display the converted ethereum address
            if (document.getElementById("validicon2").style.display == 'block'){
                document.getElementById("AddressOutput").textContent = data.msg;
                document.getElementById("copyMnemButton").style.visibility = 'visible';
            }
            // If the input mnemonic was invalid inform the user accordingly
            else{
                document.getElementById("AddressOutput").textContent = 'Invalid Mnemonic';
            }
            document.getElementById("AddressOutput").style = "font-size: 20px;";
            },
        // If the ajax function fails do nothing
        failure: function () {
            }
        });
});