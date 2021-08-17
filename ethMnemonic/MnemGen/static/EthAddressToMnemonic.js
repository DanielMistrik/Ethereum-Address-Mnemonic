// Function that is called when the ethereum address conversion form is submitted
$('#EthIn').on('submit', function(e){
    e.preventDefault();
    // Ajax request to call the python function that converts the ethereum address into a mnemonic
    $.ajax({
        type: "POST",
        url: post_link_1,
        data: {
            addrss: $('#ethAddress').val(),
            csrfmiddlewaretoken: csrf_token_1,
            dataType: "json",
        },
        success: function (data) {
            // If statement determines whether the inputed ethereum address was valid
            if (document.getElementById("validicon").style.display == 'block'){
                // Prints out the mnemonic corresponding to a correct ethereum address input
                    document.getElementById("MnemonicOutput").textContent = data.msg;
                    document.getElementById("copyAddressButton").style.visibility = 'visible';
                }
                else{
                    // Informs the user the inputted address was invalid
                    document.getElementById("MnemonicOutput").textContent = 'Invalid Address';
                }
            document.getElementById("MnemonicOutput").style = "font-size: 20px;";
        },
        // If the ajax call fails do nothing
        failure: function () {
        }
    });
});
