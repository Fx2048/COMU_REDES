
# First bucket error from the bucket creation , after, this was created  again , with bucket name: awsbucketlab4bernal
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/54887920-3c0c-426a-a7de-4e713b160ed2)


# FORMAT FROM POLICY BUCKET 
````
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::<EXAMPLE-BUCKET>/*"
            ]
        }
    ]
}
````
# ARN format

```` arn:aws:s3:::awsbucketlab4bernal````

# Format text file index

````
<head>

<title> Title goes here </title>

</head>

<body bgcolor="white" text="blue">

<h1> My first page </h1> 
This is my first webpage.
</body>

</html>
````

<EXAMPLE-BUCKET>.s3-website-<REGION>.amazonaws.com

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/ad1f56e1-8a1d-4726-b8d1-ff077e7aa599)
