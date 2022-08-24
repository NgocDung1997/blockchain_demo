def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb://cluster-read:at5M8RO2IG1mFTK4c8EPfbiy@prod1.silotech.vn:28000,prod2.silotech.vn:28000,prod3.silotech.vn:28000/cluster?replicaSet=replicaset-remote&authSource=admin&readPreference=secondary&maxStalenessSeconds=120"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client['prl-box-prod-mainnet']
    
if __name__ == "__main__":    
    
    db_mainnet = get_database()
    boxes = db_mainnet['boxes'].find().limit(10)
    for box in boxes:
        print(box['_id']," | ",box['tokenId']," | ",box['ownerAddress'])