// Function that calls, via ajax, the python function that determines whether a mnemonic is valid.
function isValidMnem(){
    $.ajax({
        type : "POST",
        url: post_link_3,
        data: {
            mnem : document.getElementById("mnemonic").value,
            csrfmiddlewaretoken: csrf_token_3,
            dataType: "json",
        },
        // If the ajax call is successful a function is called that saves the asynchronous ajax's call response data
        success: function(data){
            returnajax(data.msg);
        },
        // If the ajax call fails return false as it cannot be guaranteed the mnemonic is valid.
        failure: function() {
            return false;
        }
    });
}
// Function that updates the html page with the ajax data thereby informing the user whether the inputted mnemonic is valid
function returnajax(message){
        // Display the check icon if the mnemonic is valid
        if (message=="Valid"){
        //document.getElementById("isValid").innerHTML = "Valid";
        document.getElementById("validicon2").style.display = "block";
        document.getElementById("wrongicon2").style.display = "none";
        }
        // Display the cross icon if the mnemonic is invalid
        else{
        //document.getElementById("isValid").innerHTML = "Invalid";
        document.getElementById("validicon2").style.display = "none";
        document.getElementById("wrongicon2").style.display = "block";
        }
    }