function isValid(addrss){
    if(addrss.length!=42){
        return false;
    }
    addrss = addrss.slice(2)
    var hexs = window.keccak256(addrss.toLowerCase()).toString('hex');
    for(let i = 0;i<addrss.length;i++){
        if(addrss[i].match(/[a-zA-Z]/i)){ 
            if (addrss[i] == addrss[i].toLowerCase()){
                if (parseInt(hexs[i],16)>=8){
                    return false;
                }
            }
            else{
                if (parseInt(hexs[i],16)<8){
                    return false;
                }
            }
        }
    }
    return true;
}

