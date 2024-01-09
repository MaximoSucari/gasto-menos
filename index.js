const express = require('express')
const bodyParser = require('body-parser')
const axios = require('axios')

const app = express()
const PORT = 3000
// Setup a webhook route

app.use(bodyParser.json())
app.post('/webhook', (req, res) => {
  console.log(req.body) // print all response

  messageFrom=req.body['data']['from'] // sender number
  messageMsg=req.body['data']['body'] // Message text
  console.log(req)
  res.status(200).end()
});

app.get('/', (req, res) => {
  
    console.log('hola loko')
    replyMessage(req.body)
    res.status(200).end()
})

const replyMessage = async (input) => {
    const url = 'https://graph.facebook.com/v17.0/222849127571783/messages';
    const accessToken = 'EAAX21TVIX8gBO1LGIKDKCV2hGU1LGdDQuPdQ1FZAY666KBKKczSFMZCvlMvdGewVhK3mbZAGJ8Uk1mYOZBWxUeAfMAmAY5ic4bwI6rzdDLZAMp2RIHcZAb1Nh1qInrGgPIZAcfF0SZCZC7zZAgNNgO6jnZBSO6pOYxkkY35W9ZAbbhXVV1IC4xHb8HDFDpZAwigEaN379Ips2mKDw9xgvZBJM7XQRZAZAVWdqUgZD';
    
    const headers = {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json'
    };
    
    const data = {
      "messaging_product": "whatsapp",
      "to": "541154933738",
      "type": "template",
      "template": {
        "name": "hello_world",
        "language": {
          "code": "en_US"
        }
      }
    };
    
    axios.post(url, data, { headers })
      .then(response => {
        console.log('Respuesta:', response.data);
      })
      .catch(error => {
        console.error('Error:', error);
    });
}


app.use(bodyParser.json())
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}🚀 `))





