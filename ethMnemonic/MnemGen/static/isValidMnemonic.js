function isValidMnem(){
    var obj;
    $.ajax({
    type : "POST",
    url: post_link_3,
    data: {
        mnem : document.getElementById("mnemonic").value,
        csrfmiddlewaretoken: csrf_token_3,
        dataType: "json",
    },
    success: function(data){
        returnajax(data.msg);
    },
    failure: function() {
        return false;
    }
        });
    }

    function returnajax(message){
        if (message=="Valid"){
        //document.getElementById("isValid").innerHTML = "Valid";
        document.getElementById("validicon2").style.display = "block";
        document.getElementById("wrongicon2").style.display = "none";
        }
        else{
        //document.getElementById("isValid").innerHTML = "Invalid";
        document.getElementById("validicon2").style.display = "none";
        document.getElementById("wrongicon2").style.display = "block";
        }
    }