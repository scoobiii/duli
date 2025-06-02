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


# DULI - Estrutura Completa do Projeto

```
duli-platform/
├── README.md
├── docker-compose.yml
├── docker-compose.prod.yml
├── .env.example
├── .gitignore
├── Makefile
├── skaffold.yaml
├── package.json
└── lerna.json

├── apps/
│   ├── web-frontend/                    # React/Next.js Frontend
│   │   ├── package.json
│   │   ├── next.config.js
│   │   ├── tailwind.config.js
│   │   ├── tsconfig.json
│   │   ├── .env.local.example
│   │   ├── public/
│   │   │   ├── favicon.ico
│   │   │   ├── logo.svg
│   │   │   ├── icons/
│   │   │   └── images/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── ui/
│   │   │   │   │   ├── Button.tsx
│   │   │   │   │   ├── Input.tsx
│   │   │   │   │   ├── Modal.tsx
│   │   │   │   │   ├── Loading.tsx
│   │   │   │   │   └── Treemap.tsx
│   │   │   │   ├── layout/
│   │   │   │   │   ├── Header.tsx
│   │   │   │   │   ├── Sidebar.tsx
│   │   │   │   │   ├── Footer.tsx
│   │   │   │   │   └── Layout.tsx
│   │   │   │   ├── forms/
│   │   │   │   │   ├── LoginForm.tsx
│   │   │   │   │   ├── ImageUploadForm.tsx
│   │   │   │   │   └── PatientForm.tsx
│   │   │   │   ├── medical/
│   │   │   │   │   ├── ImageViewer.tsx
│   │   │   │   │   ├── PredictionResults.tsx
│   │   │   │   │   ├── DicomViewer.tsx
│   │   │   │   │   └── ReportGenerator.tsx
│   │   │   │   └── charts/
│   │   │   │       ├── TreemapChart.tsx
│   │   │   │       ├── ConfidenceChart.tsx
│   │   │   │       └── HistoryChart.tsx
│   │   │   ├── pages/
│   │   │   │   ├── _app.tsx
│   │   │   │   ├── _document.tsx
│   │   │   │   ├── index.tsx
│   │   │   │   ├── login.tsx
│   │   │   │   ├── dashboard.tsx
│   │   │   │   ├── predictions/
│   │   │   │   │   ├── index.tsx
│   │   │   │   │   ├── new.tsx
│   │   │   │   │   └── [id].tsx
│   │   │   │   ├── patients/
│   │   │   │   │   ├── index.tsx
│   │   │   │   │   └── [id].tsx
│   │   │   │   └── reports/
│   │   │   │       ├── index.tsx
│   │   │   │       └── [id].tsx
│   │   │   ├── hooks/
│   │   │   │   ├── useAuth.ts
│   │   │   │   ├── useImageUpload.ts
│   │   │   │   ├── usePredictions.ts
│   │   │   │   └── useWebSocket.ts
│   │   │   ├── services/
│   │   │   │   ├── api.ts
│   │   │   │   ├── auth.ts
│   │   │   │   ├── predictions.ts
│   │   │   │   ├── images.ts
│   │   │   │   └── reports.ts
│   │   │   ├── utils/
│   │   │   │   ├── constants.ts
│   │   │   │   ├── helpers.ts
│   │   │   │   ├── validation.ts
│   │   │   │   └── formatters.ts
│   │   │   ├── types/
│   │   │   │   ├── api.ts
│   │   │   │   ├── user.ts
│   │   │   │   ├── prediction.ts
│   │   │   │   └── image.ts
│   │   │   └── styles/
│   │   │       ├── globals.css
│   │   │       ├── components.css
│   │   │       └── medical.css
│   │   └── tests/
│   │       ├── __mocks__/
│   │       ├── components/
│   │       ├── pages/
│   │       └── utils/
│   │
│   ├── mobile-app/                      # React Native Mobile
│   │   ├── package.json
│   │   ├── metro.config.js
│   │   ├── react-native.config.js
│   │   ├── android/
│   │   ├── ios/
│   │   └── src/
│   │       ├── components/
│   │       ├── screens/
│   │       ├── navigation/
│   │       ├── services/
│   │       ├── hooks/
│   │       └── utils/
│   │
│   └── admin-dashboard/                 # Admin React App
│       ├── package.json
│       ├── src/
│       │   ├── components/
│       │   ├── pages/
│       │   ├── services/
│       │   └── utils/
│       └── public/

├── services/                           # Backend Microservices
│   ├── api-gateway/                    # API Gateway Service
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── src/
│   │   │   ├── app.js
│   │   │   ├── routes/
│   │   │   │   ├── auth.js
│   │   │   │   ├── images.js
│   │   │   │   ├── predictions.js
│   │   │   │   └── reports.js
│   │   │   ├── middleware/
│   │   │   │   ├── auth.js
│   │   │   │   ├── rateLimit.js
│   │   │   │   ├── cors.js
│   │   │   │   └── validation.js
│   │   │   ├── config/
│   │   │   │   └── index.js
│   │   │   └── utils/
│   │   │       ├── logger.js
│   │   │       └── errorHandler.js
│   │   └── tests/
│   │
│   ├── auth-service/                   # Authentication Service
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── src/
│   │   │   ├── app.js
│   │   │   ├── controllers/
│   │   │   │   ├── authController.js
│   │   │   │   └── userController.js
│   │   │   ├── models/
│   │   │   │   ├── User.js
│   │   │   │   └── Role.js
│   │   │   ├── services/
│   │   │   │   ├── authService.js
│   │   │   │   ├── jwtService.js
│   │   │   │   └── rbacService.js
│   │   │   ├── routes/
│   │   │   │   └── authRoutes.js
│   │   │   ├── middleware/
│   │   │   │   ├── validation.js
│   │   │   │   └── security.js
│   │   │   ├── config/
│   │   │   │   ├── database.js
│   │   │   │   └── jwt.js
│   │   │   └── utils/
│   │   │       ├── encryption.js
│   │   │       └── password.js
│   │   └── tests/
│   │
│   ├── image-service/                  # Image Processing Service
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── src/
│   │   │   ├── app.py
│   │   │   ├── controllers/
│   │   │   │   ├── image_controller.py
│   │   │   │   └── dicom_controller.py
│   │   │   ├── services/
│   │   │   │   ├── image_processor.py
│   │   │   │   ├── dicom_parser.py
│   │   │   │   ├── storage_service.py
│   │   │   │   └── preprocessing.py
│   │   │   ├── models/
│   │   │   │   ├── image_model.py
│   │   │   │   └── metadata_model.py
│   │   │   ├── routes/
│   │   │   │   └── image_routes.py
│   │   │   ├── utils/
│   │   │   │   ├── validators.py
│   │   │   │   ├── converters.py
│   │   │   │   └── helpers.py
│   │   │   └── config/
│   │   │       ├── settings.py
│   │   │       └── storage.py
│   │   └── tests/
│   │
│   ├── prediction-service/             # AI Prediction Service
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── src/
│   │   │   ├── app.py
│   │   │   ├── controllers/
│   │   │   │   └── prediction_controller.py
│   │   │   ├── services/
│   │   │   │   ├── ml_service.py
│   │   │   │   ├── model_manager.py
│   │   │   │   ├── inference_service.py
│   │   │   │   └── ab_testing.py
│   │   │   ├── models/
│   │   │   │   ├── prediction_model.py
│   │   │   │   └── ml_models/
│   │   │   │       ├── covid_model.py
│   │   │   │       ├── pneumonia_model.py
│   │   │   │       └── ensemble_model.py
│   │   │   ├── routes/
│   │   │   │   └── prediction_routes.py
│   │   │   ├── utils/
│   │   │   │   ├── preprocessing.py
│   │   │   │   ├── postprocessing.py
│   │   │   │   └── metrics.py
│   │   │   └── config/
│   │   │       ├── ml_config.py
│   │   │       └── model_config.py
│   │   └── tests/
│   │
│   ├── audit-service/                  # Audit and Compliance Service
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── src/
│   │   │   ├── app.js
│   │   │   ├── controllers/
│   │   │   │   ├── auditController.js
│   │   │   │   └── complianceController.js
│   │   │   ├── services/
│   │   │   │   ├── auditService.js
│   │   │   │   ├── complianceService.js
│   │   │   │   └── reportingService.js
│   │   │   ├── models/
│   │   │   │   ├── AuditLog.js
│   │   │   │   └── ComplianceReport.js
│   │   │   ├── routes/
│   │   │   │   └── auditRoutes.js
│   │   │   └── utils/
│   │   │       ├── logger.js
│   │   │       └── encryption.js
│   │   └── tests/
│   │
│   ├── report-service/                 # Medical Report Service
│   │   ├── Dockerfile
│   │   ├── package.json
│   │   ├── src/
│   │   │   ├── app.js
│   │   │   ├── controllers/
│   │   │   │   └── reportController.js
│   │   │   ├── services/
│   │   │   │   ├── reportService.js
│   │   │   │   ├── pdfService.js
│   │   │   │   ├── hl7Service.js
│   │   │   │   └── pacsService.js
│   │   │   ├── models/
│   │   │   │   └── Report.js
│   │   │   ├── templates/
│   │   │   │   ├── medical-report.hbs
│   │   │   │   └── summary-report.hbs
│   │   │   ├── routes/
│   │   │   │   └── reportRoutes.js
│   │   │   └── utils/
│   │   │       ├── pdfGenerator.js
│   │   │       └── hl7Mapper.js
│   │   └── tests/
│   │
│   └── notification-service/           # Notification Service
│       ├── Dockerfile
│       ├── package.json
│       ├── src/
│       │   ├── app.js
│       │   ├── controllers/
│       │   │   └── notificationController.js
│       │   ├── services/
│       │   │   ├── emailService.js
│       │   │   ├── smsService.js
│       │   │   └── pushService.js
│       │   ├── templates/
│       │   │   ├── email/
│       │   │   └── sms/
│       │   └── routes/
│       │       └── notificationRoutes.js
│       └── tests/

├── infrastructure/                     # Infrastructure as Code
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── modules/
│   │   │   ├── eks/
│   │   │   ├── rds/
│   │   │   ├── s3/
│   │   │   └── vpc/
│   │   └── environments/
│   │       ├── dev/
│   │       ├── staging/
│   │       └── prod/
│   │
│   ├── kubernetes/
│   │   ├── base/
│   │   │   ├── namespace.yaml
│   │   │   ├── configmap.yaml
│   │   │   ├── secrets.yaml
│   │   │   └── rbac.yaml
│   │   ├── services/
│   │   │   ├── api-gateway/
│   │   │   │   ├── deployment.yaml
│   │   │   │   ├── service.yaml
│   │   │   │   ├── ingress.yaml
│   │   │   │   └── hpa.yaml
│   │   │   ├── auth-service/
│   │   │   ├── image-service/
│   │   │   ├── prediction-service/
│   │   │   ├── audit-service/
│   │   │   └── report-service/
│   │   └── overlays/
│   │       ├── dev/
│   │       ├── staging/
│   │       └── prod/
│   │
│   └── helm/
│       ├── duli-platform/
│       │   ├── Chart.yaml
│       │   ├── values.yaml
│       │   ├── values-dev.yaml
│       │   ├── values-staging.yaml
│       │   ├── values-prod.yaml
│       │   └── templates/
│       └── monitoring/
│           ├── prometheus/
│           ├── grafana/
│           └── elasticsearch/

├── ml-pipeline/                        # ML Pipeline and Training
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/
│   │   ├── features/
│   │   └── models/
│   │
│   ├── notebooks/
│   │   ├── exploratory-analysis.ipynb
│   │   ├── feature-engineering.ipynb
│   │   ├── model-training.ipynb
│   │   └── model-evaluation.ipynb
│   │
│   ├── src/
│   │   ├── data/
│   │   │   ├── data_loader.py
│   │   │   ├── preprocessor.py
│   │   │   └── augmentation.py
│   │   ├── features/
│   │   │   ├── feature_extractor.py
│   │   │   └── feature_selector.py
│   │   ├── models/
│   │   │   ├── base_model.py
│   │   │   ├── cnn_model.py
│   │   │   ├── resnet_model.py
│   │   │   ├── ensemble_model.py
│   │   │   └── model_registry.py
│   │   ├── training/
│   │   │   ├── trainer.py
│   │   │   ├── validator.py
│   │   │   └── hyperparameter_tuning.py
│   │   ├── evaluation/
│   │   │   ├── metrics.py
│   │   │   ├── evaluator.py
│   │   │   └── model_comparison.py
│   │   └── deployment/
│   │       ├── model_deployer.py
│   │       └── model_monitor.py
│   │
│   ├── pipelines/
│   │   ├── training_pipeline.py
│   │   ├── inference_pipeline.py
│   │   └── batch_prediction_pipeline.py
│   │
│   ├── configs/
│   │   ├── model_config.yaml
│   │   ├── training_config.yaml
│   │   └── deployment_config.yaml
│   │
│   └── requirements.txt

├── docs/                              # Documentation
│   ├── api/
│   │   ├── openapi.yaml
│   │   ├── auth-service.md
│   │   ├── image-service.md
│   │   ├── prediction-service.md
│   │   └── report-service.md
│   ├── architecture/
│   │   ├── system-design.md
│   │   ├── data-flow.md
│   │   └── security.md
│   ├── deployment/
│   │   ├── local-setup.md
│   │   ├── staging-deploy.md
│   │   └── production-deploy.md
│   ├── user-guides/
│   │   ├── medical-professional.md
│   │   ├── admin-guide.md
│   │   └── patient-guide.md
│   └── development/
│       ├── contributing.md
│       ├── coding-standards.md
│       └── testing-guide.md

├── scripts/                           # Utility Scripts
│   ├── setup/
│   │   ├── install-dependencies.sh
│   │   ├── setup-database.sh
│   │   └── generate-certificates.sh
│   ├── deployment/
│   │   ├── deploy-dev.sh
│   │   ├── deploy-staging.sh
│   │   └── deploy-prod.sh
│   ├── maintenance/
│   │   ├── backup-database.sh
│   │   ├── clean-storage.sh
│   │   └── update-models.sh
│   └── monitoring/
│       ├── health-check.sh
│       └── performance-test.sh

├── tests/                             # Integration and E2E Tests
│   ├── integration/
│   │   ├── api-gateway.test.js
│   │   ├── auth-flow.test.js
│   │   ├── prediction-flow.test.js
│   │   └── report-generation.test.js
│   ├── e2e/
│   │   ├── user-journey.test.js
│   │   ├── medical-workflow.test.js
│   │   └── admin-workflow.test.js
│   └── performance/
│       ├── load-test.js
│       └── stress-test.js

├── monitoring/                        # Monitoring and Observability
│   ├── prometheus/
│   │   ├── prometheus.yml
│   │   └── rules/
│   ├── grafana/
│   │   ├── dashboards/
│   │   │   ├── system-overview.json
│   │   │   ├── ml-performance.json
│   │   │   └── business-metrics.json
│   │   └── provisioning/
│   ├── elasticsearch/
│   │   └── logstash/
│   └── jaeger/
│       └── jaeger-config.yml

└── .github/                          # GitHub Actions CI/CD
    └── workflows/
        ├── ci.yml
        ├── cd-dev.yml
        ├── cd-staging.yml
        ├── cd-prod.yml
        ├── security-scan.yml
        └── dependency-update.yml
```

## 📋 Resumo da Estrutura

### **Frontend Apps**
- **web-frontend**: React/Next.js para médicos e profissionais
- **mobile-app**: React Native para uso móvel
- **admin-dashboard**: Interface administrativa

### **Backend Services**
- **api-gateway**: Ponto único de entrada
- **auth-service**: Autenticação e autorização
- **image-service**: Processamento de imagens médicas
- **prediction-service**: IA e predições
- **audit-service**: Auditoria e compliance
- **report-service**: Geração de relatórios médicos
- **notification-service**: Notificações

### **Infrastructure**
- **terraform**: Infraestrutura como código
- **kubernetes**: Orquestração de containers
- **helm**: Gerenciamento de aplicações K8s

### **ML Pipeline**
- Pipeline completo de treinamento
- Notebooks para análise
- Modelos e experimentos
- Deploy automatizado

### **DevOps & Monitoring**
- CI/CD com GitHub Actions
- Monitoramento com Prometheus/Grafana
- Logs centralizados com ELK Stack
- Testes automatizados




