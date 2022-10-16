from DeepMTP.utils.utils import generate_config

def test_generate_config():
    
    original_config = {
        'instance_branch_input_dim': 10,
        'target_branch_input_dim': 15,
        'validation_setting': 'B',
        'general_architecture_version': 'dot_product',
        'problem_mode': 'classification',
        'learning_rate': 0.001,
        'decay': 0,
        'batch_norm': False,
        'dropout_rate': 0,
        'momentum': 0.9,
        'weighted_loss': False,
        'compute_mode': 'cuda:7',
        'train_batchsize': 512,
        'val_batchsize': 512,
        'num_epochs': 50,
        'num_workers': 4,
        'metrics': ['hamming_loss', 'auroc'],
        'metrics_average': ['macro'],
        'patience': 10,

        'evaluate_train': True,
        'evaluate_val': True,

        'verbose': True,
        'results_verbose': False,
        'use_early_stopping': True,
        'use_tensorboard_logger': True,
        'wandb_project_name': 'Dummy_Project',
        'wandb_project_entity': 'username',
        'metric_to_optimize_early_stopping': 'loss',
        'metric_to_optimize_best_epoch_selection': 'loss',

        'instance_branch_architecture': 'MLP',
        'use_instance_features': False,

        'instance_branch_nodes_reducing_factor': 2,
        'instance_branch_nodes_per_layer': [123, 100],
        'instance_branch_layers': None,

        'target_branch_architecture': 'MLP',
        'use_target_features': False,

        'target_branch_nodes_reducing_factor': 2,
        'target_branch_nodes_per_layer': [132, 100],
        'target_branch_layers': None,

        
        'embedding_size': 30,
        'comb_mlp_nodes_reducing_factor': 2,
        'comb_mlp_nodes_per_layer': [2048, 2048, 2048],
        'comb_mlp_layers': None, 

        'save_model': True,

        'eval_every_n_epochs': 10,
        'delta': 0,
        'eval_instance_verbose': False,
        'eval_target_verbose': False,
        'return_results_per_target': False,
        'results_path': './results/',
        'experiment_name': None,
        'load_pretrained_model': False,
        'pretrained_model_path': '',
        'instance_train_transforms': None,
        'instance_inference_transforms': None,
        'target_train_transforms': None,
        'target_inference_transforms': None,
        'running_hpo': False,
        'hpo_results_path': './',
        'additional_info': {}
    }
    
    config = generate_config(    
        instance_branch_input_dim = original_config['instance_branch_input_dim'],
        target_branch_input_dim = original_config['target_branch_input_dim'],
        validation_setting = original_config['validation_setting'],
        general_architecture_version = 'dot_product',
        problem_mode = original_config['problem_mode'],
        learning_rate = 0.001,
        decay = 0,
        batch_norm = False,
        dropout_rate = 0,
        momentum = 0.9,
        weighted_loss = False,
        compute_mode = 'cuda:7',
        train_batchsize = 512,
        val_batchsize = 512,
        num_epochs = 50,
        num_workers = 4,
        # metrics = ['hamming_loss', 'auroc', 'f1_score', 'aupr', 'accuracy', 'recall', 'precision'],
        # metrics_average = ['macro', 'micro'],
        metrics = ['hamming_loss', 'auroc'],
        metrics_average = ['macro'],
        patience = 10,

        evaluate_train = True,
        evaluate_val = True,

        verbose = True,
        results_verbose = False,
        use_early_stopping = True,
        use_tensorboard_logger = True,
        wandb_project_name = 'Dummy_Project',
        wandb_project_entity = 'username',
        metric_to_optimize_early_stopping = 'loss',
        metric_to_optimize_best_epoch_selection = 'loss',

        instance_branch_architecture = 'MLP',
        use_instance_features = False,
        instance_branch_params = {
            'instance_branch_nodes_reducing_factor': 2,
            'instance_branch_nodes_per_layer': [123, 100],
            'instance_branch_layers': None,
            # 'instance_branch_conv_architecture': 'resnet',
            # 'instance_branch_conv_architecture_version': 'resnet101',
            # 'instance_branch_conv_architecture_dense_layers': 1,
            # 'instance_branch_conv_architecture_last_layer_trained': 'last',
        },


        target_branch_architecture = 'MLP',
        use_target_features = False,
        target_branch_params = {
            'target_branch_nodes_reducing_factor': 2,
            'target_branch_nodes_per_layer': [132, 100],
            'target_branch_layers': None,
            # 'target_branch_conv_architecture': 'resnet',
            # 'target_branch_conv_architecture_version': 'resnet101',
            # 'target_branch_conv_architecture_dense_layers': 1,
            # 'target_branch_conv_architecture_last_layer_trained': 'last',
        },
        
        embedding_size = 30,
        comb_mlp_nodes_reducing_factor = 2,
        comb_mlp_nodes_per_layer = [2048, 2048, 2048],
        comb_mlp_layers = None, 

        save_model = True,

        eval_every_n_epochs = 10,

        additional_info = {}
    )
    assert len(config) == len(original_config)
    for k,v in config.items():
        assert k in original_config
        assert v == original_config[k]
        
    # assert config == original_config