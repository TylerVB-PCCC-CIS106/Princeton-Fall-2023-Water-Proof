const apiKey = 'sk_live_990a5e0b-ae24-49fc-bd59-bd903693aa4a';
const url = 'https://api.verbwire.com/v1/nft/userOps/nftsMinted';

const searchBtn = document.getElementById('searchBtn');
const searchInput = document.getElementById('searchInput');
const output = document.getElementById('output');

async function fetchVerbwireData() {
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-API-Key': apiKey
        }
    });
    const data = await response.json();
    console.log(data.nfts_minted["NFT details"].length-1);
    const nft_ifps_url  = await fetch(data.nfts_minted["NFT details"][data.nfts_minted["NFT details"].length-1].startTokenURI, {
        method: 'GET',
    })

    const nft_ifps_url_data = await nft_ifps_url.json();
    const trait_data = nft_ifps_url_data.attributes[0];


    if(JSON.parse(trait_data.replace(/'/g, '"')).value==searchInput.value){
        const ipfsImage = nft_ifps_url_data.image;
        const token = ipfsImage.slice(7);
        console.log('https://ipfs.io/ipfs/'+token);
        await fetch('https://ipfs.io/ipfs/'+token, {
            method: 'GET',
        })


        .then((response) => response.text())
        .then((text) => output.innerHTML=text);
    }
    else{
        output.innerHTML = "No Data found";
    }
}


searchBtn.addEventListener('click', fetchVerbwireData);