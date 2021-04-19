allow(user: accounts::CustomUser, "read", _region: communities::Region ) if 
    user.status_type="MANAGER";