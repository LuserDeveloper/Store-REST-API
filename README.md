# Store-REST-API

API is Live at https://stores-restful-flask-api.herokuapp.com

URL | Type | Usage
--- | --- | ---
/register | POST | To register a New User
/user/[id] | GET | To have UserInfo having specified [id]
/auth | POST | To authenticate and get access token
/user/[id] | DELETE | To delete User having specified [id]
/item/[item-name] | POST | To create Item with specified name
/item/[item-name] | GET | To get ItemInfo with specified name
/items | GET | To get all Items Info 
/item/[item-name] | PUT | To update Item data with specified name
/item/[item-name] | DELETE | To delete Item with specified name
/store/[store-name] | POST | To create Store with specified name
/store/[store-name] | GET | To get StoreInfo with specified name
/stores | GET | To get all Stores Info
/store/[store-name] | DELETE | To delete Store with specified name

