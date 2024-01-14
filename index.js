const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const PORT = 3000;
// Setup a webhook route

app.use(bodyParser.json());
app.post("/webhook", async (req, res) => {
  const exampleReq = {
    event_type: "message_received",
    instanceId: "1150",
    data: {
      id: "false_17692426345@c.us_3EB0FF54790702367270",
      from: "+5491154933738",
      to: "+5491124043250",
      ack: "",
      type: "chat",
      body: "2400 café con Polo",
      fromMe: false,
      time: 1644957719,
    },
  };

  return validateMessage(req.body);
});

const validateMessage = async (message) => {
  try {
    const { data } = message;

    // Check if the message is from a new user or from an already registered user
    await responseRouter(data);

    res.status(200).end();
  } catch (error) {
    res.status(500).send({
      message: error,
    });
  }
};

const responseRouter = async (data) => {
  // query user database and check if the phoneNumber is already registered
  // const user = await getUserByPhoneNumber(data.from)
  if (user) {
    if (user && user.password) {
      return analyzeExpenseReceived(data.body);
    }
    await sendRegisterMessage(user);
  }
  return await sendWelcomeMessage(data.from);
};

const sendWelcomeMessage = async (number) => {
  //TODO: Define welcomeMessage by envirmoment variable
  const message = `Bienvenido a GastaMenos!`;
  await sender(number, message);
};

const sendRegisterMessage = async (number) => {
  //TODO: Define registerMessage by envirmoment variable
  const message = `Hola loko! Para analizar tus gastos vamos a necesitar que te registres :) \n Elegí una constraseña`;
  await sender(number, message);
};

const analyzeExpenseReceived = (message) => {
  return message;
};

const sender = async (number, body) => {
  /*  const url = "https://graph.facebook.com/v17.0/222849127571783/messages";
  const accessToken =
    "EAAX21TVIX8gBO1LGIKDKCV2hGU1LGdDQuPdQ1FZAY666KBKKczSFMZCvlMvdGewVhK3mbZAGJ8Uk1mYOZBWxUeAfMAmAY5ic4bwI6rzdDLZAMp2RIHcZAb1Nh1qInrGgPIZAcfF0SZCZC7zZAgNNgO6jnZBSO6pOYxkkY35W9ZAbbhXVV1IC4xHb8HDFDpZAwigEaN379Ips2mKDw9xgvZBJM7XQRZAZAVWdqUgZD";

  const headers = {
    Authorization: `Bearer ${accessToken}`,
    "Content-Type": "application/json",
  }; */
  /*   axios
      .post(url, data, { headers })
      .then((response) => {
        console.log("Respuesta:", response.data);
      })
      .catch((error) => {
        console.error("Error:", error);
      }); */
};

app.use(bodyParser.json());
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}🚀 `));
