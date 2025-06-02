### Projeto DULI 

graph TB
    subgraph "Interface do Usuário"
        UI[Streamlit Web Interface]
        Upload[Upload de Imagem]
        URL[URL Input]
        Webcam[Webcam Capture]
    end
    
    subgraph "Processamento"
        PIL[PIL Image Processing]
        Numpy[NumPy Array Processing]
        TM[Teachable Machine Model]
    end
    
    subgraph "Visualização"
        Plotly[Plotly Treemap]
        Results[Results Display]
    end
    
    subgraph "Dados de Treinamento"
        DS1[COVID-19 Dataset]
        DS2[SARS Dataset]
        DS3[Pneumonia Dataset]
        DS4[Normal X-ray Dataset]
        DSN[Multiple Pathology Datasets]
    end
    
    subgraph "Modelo Atual"
        TMModel[TensorFlow via Teachable Machine]
        Classes[20+ Pathology Classes]
    end
    
    UI --> Upload
    UI --> URL
    UI --> Webcam
    
    Upload --> PIL
    URL --> PIL
    Webcam --> PIL
    
    PIL --> Numpy
    Numpy --> TM
    
    DS1 --> TMModel
    DS2 --> TMModel
    DS3 --> TMModel
    DS4 --> TMModel
    DSN --> TMModel
    
    TMModel --> TM
    TM --> Classes
    Classes --> Plotly
    Plotly --> Results
    Results --> UI
    
    style TMModel fill:#ffcccc
    style TM fill:#ffcccc
    style UI fill:#ccffcc
    style Plotly fill:#ccccff




		classDiagram
    class StreamlitApp {
        +main()
        +load_model()
        +process_image()
        +display_results()
    }
    
    class ImageProcessor {
        +preprocess_image(image)
        +resize_image(image, size)
        +normalize_pixels(image)
        +convert_to_array(image)
    }
    
    class TeachableMachineModel {
        +model_url: string
        +labels: list
        +predict(image_array)
        +get_predictions()
    }
    
    class ResultsVisualizer {
        +create_treemap(predictions)
        +format_results(data)
        +display_probabilities()
    }
    
    class DatasetHandler {
        +covid_dataset: list
        +sars_dataset: list
        +pneumonia_dataset: list
        +normal_dataset: list
        +load_datasets()
    }
    
    StreamlitApp --> ImageProcessor
    StreamlitApp --> TeachableMachineModel
    StreamlitApp --> ResultsVisualizer
    TeachableMachineModel --> DatasetHandler
    
    ImageProcessor : PIL Library
    ResultsVisualizer : Plotly Library
    TeachableMachineModel : TensorFlow Backend



graph TB
    subgraph "Frontend Layer"
        WebApp[React/Next.js Web App]
        MobileApp[React Native Mobile]
        API_Gateway[API Gateway]
    end
    
    subgraph "Authentication & Security"
        Auth[OAuth 2.0 / JWT]
        RBAC[Role-Based Access Control]
        Encrypt[End-to-End Encryption]
    end
    
    subgraph "Business Logic Layer"
        UserService[User Management Service]
        ImageService[Image Processing Service]
        PredictionService[AI Prediction Service]
        AuditService[Medical Audit Service]
        ReportService[Report Generation Service]
    end
    
    subgraph "AI/ML Layer"
        ModelRegistry[ML Model Registry]
        TensorFlowServing[TensorFlow Serving]
        ModelVersioning[Model Versioning]
        ABTesting[A/B Testing Framework]
    end
    
    subgraph "Data Layer"
        PostgreSQL[(PostgreSQL - User Data)]
        MongoDB[(MongoDB - Images & Metadata)]
        S3[AWS S3 - Image Storage]
        Redis[(Redis - Cache)]
    end
    
    subgraph "External Services"
        PACS[PACS Integration]
        HL7[HL7 FHIR API]
        Regulatory[ANVISA Compliance API]
        Monitoring[CloudWatch/DataDog]
    end
    
    subgraph "MLOps Pipeline"
        DataPipeline[Data Ingestion Pipeline]
        Training[Automated Training Pipeline]
        Validation[Model Validation Service]
        Deployment[Automated Deployment]
    end
    
    WebApp --> API_Gateway
    MobileApp --> API_Gateway
    API_Gateway --> Auth
    Auth --> RBAC
    
    API_Gateway --> UserService
    API_Gateway --> ImageService
    API_Gateway --> PredictionService
    API_Gateway --> ReportService
    
    ImageService --> MongoDB
    ImageService --> S3
    UserService --> PostgreSQL
    PredictionService --> Redis
    
    PredictionService --> TensorFlowServing
    TensorFlowServing --> ModelRegistry
    ModelRegistry --> ModelVersioning
    
    AuditService --> PostgreSQL
    AuditService --> Regulatory
    
    PACS --> ImageService
    HL7 --> UserService
    
    DataPipeline --> Training
    Training --> Validation
    Validation --> Deployment
    Deployment --> ModelRegistry
    
    Monitoring --> UserService
    Monitoring --> ImageService
    Monitoring --> PredictionService
    
    style Auth fill:#ff9999
    style RBAC fill:#ff9999
    style Encrypt fill:#ff9999
    style TensorFlowServing fill:#99ff99
    style ModelRegistry fill:#99ff99
    style AuditService fill:#9999ff


graph TB
    subgraph "Frontend Layer"
        WebApp[React/Next.js Web App]
        MobileApp[React Native Mobile]
        API_Gateway[API Gateway]
    end
    
    subgraph "Authentication & Security"
        Auth[OAuth 2.0 / JWT]
        RBAC[Role-Based Access Control]
        Encrypt[End-to-End Encryption]
    end
    
    subgraph "Business Logic Layer"
        UserService[User Management Service]
        ImageService[Image Processing Service]
        PredictionService[AI Prediction Service]
        AuditService[Medical Audit Service]
        ReportService[Report Generation Service]
    end
    
    subgraph "AI/ML Layer"
        ModelRegistry[ML Model Registry]
        TensorFlowServing[TensorFlow Serving]
        ModelVersioning[Model Versioning]
        ABTesting[A/B Testing Framework]
    end
    
    subgraph "Data Layer"
        PostgreSQL[(PostgreSQL - User Data)]
        MongoDB[(MongoDB - Images & Metadata)]
        S3[AWS S3 - Image Storage]
        Redis[(Redis - Cache)]
    end
    
    subgraph "External Services"
        PACS[PACS Integration]
        HL7[HL7 FHIR API]
        Regulatory[ANVISA Compliance API]
        Monitoring[CloudWatch/DataDog]
    end
    
    subgraph "MLOps Pipeline"
        DataPipeline[Data Ingestion Pipeline]
        Training[Automated Training Pipeline]
        Validation[Model Validation Service]
        Deployment[Automated Deployment]
    end




    
    WebApp --> API_Gateway
    MobileApp --> API_Gateway
    API_Gateway --> Auth
    Auth --> RBAC
    
    API_Gateway --> UserService
    API_Gateway --> ImageService
    API_Gateway --> PredictionService
    API_Gateway --> ReportService
    
    ImageService --> MongoDB
    ImageService --> S3
    UserService --> PostgreSQL
    PredictionService --> Redis
    
    PredictionService --> TensorFlowServing
    TensorFlowServing --> ModelRegistry
    ModelRegistry --> ModelVersioning
    
    AuditService --> PostgreSQL
    AuditService --> Regulatory
    
    PACS --> ImageService
    HL7 --> UserService
    
    DataPipeline --> Training
    Training --> Validation
    Validation --> Deployment
    Deployment --> ModelRegistry
    
    Monitoring --> UserService
    Monitoring --> ImageService
    Monitoring --> PredictionService
    
    style Auth fill:#ff9999
    style RBAC fill:#ff9999
    style Encrypt fill:#ff9999
    style TensorFlowServing fill:#99ff99
    style ModelRegistry fill:#99ff99
    style AuditService fill:#9999ff



sequenceDiagram
    participant User as Usuário/Médico
    participant Frontend as Frontend App
    participant Gateway as API Gateway
    participant Auth as Auth Service
    participant ImageSvc as Image Service
    participant PredSvc as Prediction Service
    participant MLModel as ML Model
    participant AuditSvc as Audit Service
    participant Database as Database
    participant Storage as Cloud Storage
    
    User->>Frontend: Upload X-ray/CT Image
    Frontend->>Gateway: POST /api/v1/predictions
    Gateway->>Auth: Validate JWT Token
    Auth-->>Gateway: Token Valid
    
    Gateway->>ImageSvc: Process Image Upload
    ImageSvc->>Storage: Store Original Image
    Storage-->>ImageSvc: Storage URL
    ImageSvc->>ImageSvc: Preprocess Image
    ImageSvc->>Database: Save Image Metadata
    ImageSvc-->>Gateway: Image Processed (imageId)
    
    Gateway->>PredSvc: Predict Pathology (imageId)
    PredSvc->>ImageSvc: Get Preprocessed Image
    ImageSvc-->>PredSvc: Preprocessed Image Data
    
    PredSvc->>MLModel: Run Prediction
    MLModel-->>PredSvc: Prediction Results
    
    PredSvc->>Database: Save Prediction Results
    PredSvc->>AuditSvc: Log Prediction Event
    AuditSvc->>Database: Store Audit Log
    
    PredSvc-->>Gateway: Prediction Results
    Gateway-->>Frontend: JSON Response
    Frontend->>Frontend: Render Treemap Visualization
    Frontend-->>User: Display Results
    
    Note over User,Storage: Async processes
    AuditSvc->>AuditSvc: Generate Compliance Report
    MLModel->>MLModel: Monitor Model Performance
    ImageSvc->>ImageSvc: Clean Temporary Files



graph TB
    subgraph "Development Environment"
        DevTeam[Development Team]
        GitRepo[Git Repository]
        LocalTesting[Local Testing]
    end
    
    subgraph "CI/CD Pipeline"
        GithubActions[GitHub Actions]
        UnitTests[Unit Tests]
        IntegrationTests[Integration Tests]
        SecurityScan[Security Scanning]
        DockerBuild[Docker Build]
        ContainerRegistry[Container Registry]
    end
    
    subgraph "Staging Environment"
        StagingK8s[Kubernetes Staging]
        StagingDB[Staging Database]
        StagingML[Staging ML Models]
        LoadTesting[Load Testing]
    end
    
    subgraph "Production Environment - AWS"
        EKS[Amazon EKS Cluster]
        ALB[Application Load Balancer]
        
        subgraph "Microservices"
            AuthPod[Auth Service Pods]
            ImagePod[Image Service Pods]
            PredPod[Prediction Service Pods]
            AuditPod[Audit Service Pods]
        end
        
        subgraph "Data Layer"
            RDS[Amazon RDS PostgreSQL]
            DocumentDB[Amazon DocumentDB]
            S3Bucket[Amazon S3]
            ElastiCache[Amazon ElastiCache Redis]
        end
        
        subgraph "ML Infrastructure"
            SageMaker[Amazon SageMaker]
            ECR[Amazon ECR]
            Lambda[AWS Lambda Functions]
        end
        
        subgraph "Monitoring & Logging"
            CloudWatch[Amazon CloudWatch]
            XRay[AWS X-Ray]
            ElasticSearch[Amazon Elasticsearch]
        end
    end
    
    subgraph "External Integrations"
        PACS_System[PACS System]
        HL7_API[HL7 FHIR APIs]
        ANVISA_API[ANVISA Compliance API]
    end
    
    DevTeam --> GitRepo
    GitRepo --> GithubActions
    
    GithubActions --> UnitTests
    GithubActions --> IntegrationTests
    GithubActions --> SecurityScan
    
    UnitTests --> DockerBuild
    IntegrationTests --> DockerBuild
    SecurityScan --> DockerBuild
    
    DockerBuild --> ContainerRegistry
    ContainerRegistry --> StagingK8s
    
    StagingK8s --> StagingDB
    StagingK8s --> StagingML
    StagingK8s --> LoadTesting
    
    LoadTesting --> EKS
    ContainerRegistry --> EKS
    
    ALB --> AuthPod
    ALB --> ImagePod
    ALB --> PredPod
    ALB --> AuditPod
    
    AuthPod --> RDS
    ImagePod --> DocumentDB
    ImagePod --> S3Bucket
    PredPod --> ElastiCache
    PredPod --> SageMaker
    AuditPod --> RDS
    
    SageMaker --> ECR
    Lambda --> S3Bucket
    
    CloudWatch --> AuthPod
    CloudWatch --> ImagePod
    CloudWatch --> PredPod
    CloudWatch --> AuditPod
    
    XRay --> EKS
    ElasticSearch --> CloudWatch
    
    EKS --> PACS_System
    EKS --> HL7_API
    EKS --> ANVISA_API
    
    style EKS fill:#ff9999
    style SageMaker fill:#99ff99
    style RDS fill:#9999ff
    style CloudWatch fill:#ffff99




