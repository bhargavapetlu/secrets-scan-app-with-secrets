const stripeKey = "sk_test_51H8DUMMYKEYqwertyuiopasdfgh";
const firebaseConfig = {
  apiKey: "AIzaSyDUMMY-FirebaseKey-123456",
  authDomain: "myapp.firebaseapp.com",
  projectId: "myapp"
};

function initApp() {
  console.log("Stripe Key:", stripeKey);
  console.log("Firebase Key:", firebaseConfig.apiKey);
}
initApp();
