// Function that determines whether a given ethereum address is valid as per EIP-55.
function isValid(addrss){
    // An address of wrong length, in this case the address must also have the prefix 0x, is immediately denied
    if(addrss.length!=42){
        return false;
    }
    // The 0x prefix is taken out
    addrss = addrss.slice(2)
    // The address is made all lowercase and its keccak hash in generated
    var hexs = window.keccak256(addrss.toLowerCase()).toString('hex');
    // Iterates over the address to find alphabet letters so it can use EIP-55 capital letter checksum
    for(let i = 0;i<addrss.length;i++){
        if(addrss[i].match(/[a-zA-Z]/i)){
            // If the addresses alphabet is lowercase it verifies the adjacent hash character is less than 8 otherwise
            // the checksum fails
            if (addrss[i] == addrss[i].toLowerCase()){
                if (parseInt(hexs[i],16)>=8){
                    return false;
                }
            }
            // If the addresses alphabet is uppercase it verifies the adjacent hash character is less than 8 otherwise
            // the checksum fails
            else{
                if (parseInt(hexs[i],16)<8){
                    return false;
                }
            }
        }
    }
    return true;
}

