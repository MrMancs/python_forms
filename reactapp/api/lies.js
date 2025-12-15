export default async function handler(req, res) {
  const method = req.method;
  if (method == "POST") {
    const body = req.body;
    console.log("Body: ", body);
    return res.sendStatus(201);
  } else {
    return res.sendStatus(405);
  }
}